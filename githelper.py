#!/usr/bin/env python

import os
import shelve
import subprocess
from getpass import getpass

user_home = os.environ['HOME']
credentials_path = user_home + '/.githelperdata'
key_id = os.getcwd()

if __name__ == '__main__':

    data = shelve.open(credentials_path, writeback=True)
    os.chmod(credentials_path, 0o600)

    username = input("Username: ")
    password = getpass("Password: ")

    key_exists = key_id in data

    if key_exists:
        data[key_id] = username + ';' + password
    else:
        data[key_id] = username + ';' + password

    data.close()

subprocess.run(["git", "config", "credential.helper", "shell"])
