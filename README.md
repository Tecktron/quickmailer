# Quickmailer
A simple command line script to send SMTP email using [Django](https://www.djangoproject.com/). I built this for several
reasons, one being I had a need for it, and another to show how simple it is to leverage all the django goodness even if
you're not using django as a server.

## Requirements:
- Python 3.x
- Django
- Access to an SMTP server

### Setup
Install Django into your environment
Update the `base/settings.py` file with your smtp server credentials, or better yet, create a `base/local_settings.py`
and override them.

### Run
Simply run `python quickmail.py` from the command line.
Use `-h` option for help.

#### Examples

**Simple Message:**

`python3 quickmail.py -m "This is a test" -s "Testing" -t "you@example.com" "someone@exmple.com`


**HTML Message from a file:**

`python3 quickmail.py -m /path/to/test_msg.html -w -s "Testing" -t "you@example.com"`

**Simple HTML:**

`python3 quickmail.py -m "<p><b>Simple HTML</b><br>This works as well</p>" -w -s "Testing" -t "you@example.com"`

**Send Attachements:**

`python3 quickmail.py -m "This is a test" -a "/path/to/somefile.doc" "/path/to/someimage.png" -s "Testing" -t "you@example.com"`


### Stay Tuned...
Again, I built this as an example of possibilities as well as out of use.
However I find myself using this more and more and I have plans to turn this into a full fledged app very soon.
It will still support commandline use in the same way, plus (or maybe only) through the Django admin interface (`manage.py`). I'm also
going to implement using the Django templeting system to send HTML emails. Again, this will all as simple as possible to
you, the user. But for now, please enjoy this as is. More to come, so thanks for watching and as always, your star is appreciated.
