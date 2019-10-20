#!/bin/bash

REPO=$(basename $PWD)

read -p 'Username: ' uservar
read -sp 'Password: ' passvar
echo

touch $HOME/.githelperdata.txt

# check if credencial exists
cat $HOME/.githelperdata.txt | grep $REPO > /dev/null
# if so... update
if [ $? -eq 0 ] ; then
  sed -i "s/${REPO}.*/${REPO};${uservar};${passvar}/" $HOME/.githelperdata.txt
# if not... create
else
  echo "$REPO;$uservar;$passvar" >> $HOME/.githelperdata.txt
fi

chmod 0600 $HOME/.githelperdata.txt
git config credential.helper shell