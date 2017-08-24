#!/usr/bin/python3

"""The main objective of this script is to setup all config files for Linux machines.

Documentation style: https://www.python.org/dev/peps/pep-0008/
"""

from __future__ import print_function     # Keep Python 2 inline with Python 3
import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
import sys  # This allows for user input
import shutil
import errno
from sys import version_info
from pathlib import Path  # Need to re-write for python 2


def sync_repo():
    path = "~/GIT/Python/relaypi"
    os.path.expanduser(path) # This allows for us to use the home directory shortcut(~).
    os.system("git pull")
    print("Repo sync has completed.")
    send_email()


def send_email():
    fromaddr = "raythomas@gmail.com"
    toaddr = "raythomas@live.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Sync has completed"

    body = "RelayPi Sync has completed"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "nofhenvpxqdkfjae")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()




def main():
    sync_repo()


"""This will only execute the main method, so if there is code that needs to be executed, \
    it must go thru main"""
if __name__ == "__main__":
    main()