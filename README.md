# Overview

...

# Install

The installer will create the directory `$HOME/bin` and copy the scripts `git-credential-shell.py` and `githelper.py` to it.

```
chmod 755 installer.sh && ./installer.sh
```

# Usage

- To configure credential input the username and password in the working copy of a git repo

```
githelper
```

The helper will create the file `$HOME/.githelperdata` to store the credential, it will use the path of the current directory as ID

- To remove credential and helper from current git repo:

```
githelper -r
```

- To remove credential and helper from specific git repo, you can use `-l` to get the list of repos:

```
githelper -r -c /path/to/repo
```

- To list all the credentials stored:

```
githelper -l
```

# To-Do

- ~~List credentials~~
- Encrypt git credentials
- ~~Delete credential from current repo~~
- ~~Delete credential from repo using ID~~

# Links

- https://github.com/njvrzm/git-credential-shell