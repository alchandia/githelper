# Overview

...

# Install

The installer will create the directory `$HOME/bin` and copy the scripts `git-credential-shell.py` and `githelper.py` to it.

```
chmod 755 installer.sh && ./installer.sh
```

# Usage

In the working copy of the git repo, run this command and input the user and password:

```
githelper
```

The helper will create the file `$HOME/.githelperdata` to store the credential, it will use the path of the current directory as ID

To remove helper from a git repo:

```
git config --unset credential.helper
```

# To-Do

- Encrypt git credentials

# Links

- https://github.com/njvrzm/git-credential-shell