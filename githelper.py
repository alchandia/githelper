#!/usr/bin/env python3

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
    parser = argparse.ArgumentParser(description="Parses command")
    parser.add_argument('-l', '--list', action='store_true', help="List credentials")
    parser.add_argument('-r', '--remove', action='store_true', help="Remove credential")
    parser.add_argument('-c', '--credential', type=str, help="Credential ID to remove")
    options = parser.parse_args(args)
    return options


if __name__ == '__main__':

    arguments = get_options(sys.argv[1:])
    final_error = ''

    try:

        data = shelve.open(credentials_path, writeback=True)
        os.chmod(credentials_path, 0o600)

        if arguments.remove:
            final_error = "Error deleting credential"
            if arguments.credential is None:
                key_searched = key_id
            else:
                key_searched = arguments.credential

            key_exists = key_searched in data
            if key_exists:
                del data[key_searched]
                subprocess.run(["git", "config", "--unset", "credential.helper"], cwd=key_searched)
                print("Credential for " + key_searched + " deleted")
            else:
                print("Credential for " + key_searched + " doesn't exists")

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

    except Exception as e:
        print("Some exception occurred: " + e)
        sys.exit(final_error)
    finally:
        data.close()
        sys.exit()
