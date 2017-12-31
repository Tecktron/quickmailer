import argparse
import os
import re
import sys

if __name__ == "__main__":
    if sys.version_info < (3, 0):
        print("This script requires version 3+ of python. Please try running it with command 'python3' instead")
        exit(8)

    parser = argparse.ArgumentParser(
        description="Quick Mailer"
    )
    parser.add_argument("-m", "--message", dest="msg", type=str, required=True,
                        help="The plain text message or filename of a message to send")
    parser.add_argument("-t", "--to", dest="to", nargs="+", metavar="email@domain.com", type=str,
                        help="Email address to recieve the message", required=True)
    parser.add_argument("-f", "--from", dest="sender", type=str, required=False,
                        help="The from Email, if not provided, the settings will be used. NOTE: A specific address may "
                             "be required by your SMTP server")
    parser.add_argument("-s", "--subject", dest="subject", required=True, type=str, help="The subject line")
    parser.add_argument("-w", "--html", dest="html", action="store_true", required=False,
                        help="If using a file for m and file is html set this flag to use html email")
    parser.add_argument("-a", "--attach", dest="attach", metavar="/path/to/file.txt", nargs="*", required=False,
                        help="files to attach (use full path)", default=[])

    args = parser.parse_args()

    # Here we inject the settings and load django
    if not os.environ.get("DJANGO_SETTINGS_MODULE", False):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
    try:
        import django
        from django.conf import settings
    except ImportError:
        django = None
        settings = None
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )

    django.setup()
    # don't import Django things until after setup or errors abound
    from django.core.mail import EmailMessage, EmailMultiAlternatives
    from django.utils.html import strip_tags

    msg = ""
    is_file = False
    if os.path.isfile(args.msg) is False:
        msg = "{}".format(args.msg)
    else:
        try:
            msg = open(args.msg).read()
        except OSError as e:
            print("Could not read msg file, exception said: {}".format(e))
            exit(4)

    sender = args.sender
    if not sender:
        sender = settings.DEFAULT_FROM_EMAIL

    if args.html:
        # quick and dirty, create a plain text version.
        # replace breaks and paragraphs with newlines
        plain = re.sub("<br\s*?>", "\n", msg)
        plain = re.sub("</p>", "\n\n", plain)
        # strip the rest of the tags.
        plain = strip_tags(plain)
        email = EmailMultiAlternatives(args.subject, plain, sender, args.to)
        email.attach_alternative(msg, "text/html")
    else:
        email = EmailMessage(args.subject, msg, sender, args.to)

    if len(args.attach):
        for attachment in args.attach:
            if os.path.isfile(attachment):
                email.attach_file(attachment)

    sent = email.send()
    if sent:
        print("Email sent successfully")
    else:
        print("There was an issue sending the message")
