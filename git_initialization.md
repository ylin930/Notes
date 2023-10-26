### Setting up git in windows

- download git (https://git-scm.com/download/win)

```console
# show where git is located after downlaod
$ git config --list --show-origin

# configure your identity
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

(can also configure other settings-but skipped for now)
```

- go to folder/file to initialize git

  ```console
  $ git init
  $ git add .
  $ git commit -m "message"
  $ git remote add origin https://github.com/ylin930/Notes #example path
  $ git push -f origin master
  or
  $ git push -u origin master
  
  (not sure what the difference is between -f and -u yet)
  ```

  