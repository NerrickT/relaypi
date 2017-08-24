#!/usr/bin/python3

"""The main objective of this script is to setup all config files for Linux machines.

Documentation style: https://www.python.org/dev/peps/pep-0008/
"""

from __future__ import print_function     # Keep Python 2 inline with Python 3
import os
import time
import sys  # This allows for user input
import shutil
import errno
from sys import version_info
from pathlib import Path  # Need to re-write for python 2


def sync_repo():
    path = "~/GIT/relaypi"
    os.chdir(path)
    os.system("git pull")
    print("Repo sync has completed.")


def main():
    sync_repo()


"""This will only execute the main method, so if there is code that needs to be executed, \
    it must go thru main"""
if __name__ == "__main__":
    main()