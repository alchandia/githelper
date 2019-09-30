#!/bin/bash

REPO=$(basename $PWD)

USER=$(cat $HOME/.githelperdata.txt | grep  "$REPO;" | cut -d ";" -f 2)
PASS=$(cat $HOME/.githelperdata.txt | grep  "$REPO;" | cut -d ";" -f 3)

echo username=$USER
echo password=$PASS