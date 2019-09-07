# Context

...

# How to use

Copy helper to path:
```
cp git-credential-shell.sh $HOME/bin/git-credential-shell
```

Create file to store credencials
```
touch $HOME/.githelperdata.txt
chmod 0600 $HOME/.githelperdata.txt
```
Set credentials in file
```
name-working-copy-directory;username;password
```

After repository clone, set credencial helper:
```
git config credential.helper shell

```
To remove helper
```
git config --unset credential.helper
```