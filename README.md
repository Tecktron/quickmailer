# Quickmailer
A simple command line script to send SMTP email using [Django](https://www.djangoproject.com/) .

## Requirements:
- Python 3.x
- Django
- Access to an SMTP server

### Setup
Update the `base/settings.py` file with your smtp server credentials.

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
