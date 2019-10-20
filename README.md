# Context

...

# Install

The installer will create the directory `$HOME/bin` and copy the scripts `git-credential-shell.sh` and `githelper.sh` to it.

```
chmod 755 installer.sh && ./installer.sh
```

# How to use

In the working copy of the git repo, run this command and input the user and password:

```
githelper
```

The helper will create the file `$HOME/.githelperdata.txt` to store the credential, it will use the name of the current directory as ID

To remove helper from a git repo:

```
git config --unset credential.helper
```

# Links

- https://github.com/njvrzm/git-credential-shell