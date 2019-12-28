#!/bin/bash

[ ! -d $HOME/bin ] && mkdir $HOME/bin

cp git-credential-shell.py $HOME/bin/git-credential-shell
cp githelper.py $HOME/bin/githelper

chmod 755 $HOME/bin/git-credential-shell
chmod 755 $HOME/bin/githelper