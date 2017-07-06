import argparse
import sys
import os

if __name__ == "__main__":
    if sys.version_info < (3, 0):
        print('This script requires version 3.5+ of python. Please try running it with command `python3` instead')
        exit(8)

    parser = argparse.ArgumentParser(
        description='Quick Mailer'
    )
    parser.add_argument('-m', '--message', dest='msg', type=str, required=True,
                        help="The plain text message or filename of a message to send")
    parser.add_argument('-t', '--to', dest='to', nargs='+', metavar='email@domain.com', type=str,
                        help="Email address to recieve the message", required=True)
    parser.add_argument('-f', '--from', dest='sender', type=str, help="The from Email. Must be enabled in the AWS config")
    parser.add_argument('-s', '--subject', dest='subject', required=True, type=str, help='The subject line')
    parser.add_argument('-w', '--html', dest='html', action='store_true', required=False,
                        help='If using a file for m and file is html set this flag to use html email')

    args = parser.parse_args()

    # Here we inject the bulk db into settings and load django
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
    from django.core.mail import send_mail

    msg = ''
    is_file = False
    if os.path.isfile(args.msg) is False:
        msg = "{}".format(args.msg)
    else:
        try:
            msg = open(args.msg).read()
            is_file = True
        except OSError as e:
            print("Could not read msg file, exception said: {}".format(e))
            exit(4)

    sender = args.sender
    if sender == '':
        sender = settings.DEFAULT_FROM_EMAIL

    if is_file and args.html:
        html_msg = 'Multipart HTML Encoded message'
        sent = send_mail(args.subject, html_msg, sender, args.to, fail_silently=False, html_message=msg)
    else:
        sent = send_mail(args.subject, msg, sender, args.to, fail_silently=False)

    if sent:
        print("Email sent successfully")
    else:
        print("There was an issue sending the message")
