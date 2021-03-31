To add a new remote to your existing repo
```
git remote add <remote_name> <remote_ssh_url>

git fetch <remote_name>
```

To push your local branch from existing repo to this new remote

```
git push -u <remote_name> <local_branch>:<remote_branch_you_want_to_create>
```
