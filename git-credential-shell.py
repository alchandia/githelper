#!/usr/bin/env python

import os
import shelve

user_home = os.environ['HOME']
credentials_path = user_home + '/.githelperdata'
key_id = os.getcwd()

if __name__ == '__main__':

    data = shelve.open(credentials_path)

    key_exists = key_id in data

    if key_exists:
        print('username=' + data[key_id].split(";")[0])
        print('password=' + data[key_id].split(";")[1])

    data.close()
