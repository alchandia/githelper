#!/usr/bin/env python

import os
import shelve
import subprocess
import argparse
import sys
from getpass import getpass
from subprocess import call, STDOUT

user_home = os.environ['HOME']
credentials_path = user_home + '/.githelperdata'
key_id = os.getcwd()


def get_options(args):
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument('-l', '--list', action='store_true', help="List credentials.")
    options = parser.parse_args(args)
    return options


if __name__ == '__main__':

    arguments = get_options(sys.argv[1:])

    data = shelve.open(credentials_path, writeback=True)
    os.chmod(credentials_path, 0o600)

    if arguments.list:
        my_keys = list(data.keys())
        my_keys.sort()
        for key in my_keys:
            print(key + ': ' + data[key])
        data.close()
    else:
        if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
            data.close()
            sys.exit("This is not a git repo!")
        else:
            username = input("Username: ")
            password = getpass("Password: ")
            data[key_id] = username + ';' + password
            subprocess.run(["git", "config", "credential.helper", "shell"])
            data.close()
