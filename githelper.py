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
    parser.add_argument('-r', '--remove', action='store_true', help="Remove current credential.")
    options = parser.parse_args(args)
    return options


if __name__ == '__main__':

    arguments = get_options(sys.argv[1:])
    final_error = ''

    try:
        data = shelve.open(credentials_path, writeback=True)
        os.chmod(credentials_path, 0o600)

        if arguments.remove:
            key_exists = key_id in data
            if key_exists:
                final_error = "Error deleting credential"
                del data[key_id]
                subprocess.run(["git", "config", "--unset", "credential.helper"])
                print("Credential for " + key_id + " deleted")
            else:
                print("Credential for " + key_id + " doesn't exists")

        if arguments.list:
            final_error = 'Error listing credentials'
            my_keys = list(data.keys())
            my_keys.sort()
            for key in my_keys:
                print(key + ': ' + data[key])

        # Default action, add/update credential
        if len(sys.argv[1:]) == 0:
            if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
                final_error = "This is not a git repo"
            else:
                final_error = "Error adding/updating credential"
                username = input("Username: ")
                password = getpass("Password: ")
                data[key_id] = username + ';' + password
                subprocess.run(["git", "config", "credential.helper", "shell"])
    except:
        sys.exit(final_error)
    finally:
        data.close()
        sys.exit()
