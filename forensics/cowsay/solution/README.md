# Solution

If you look at the given directory, we also find a .git repo. The `cowsay.py` file was just for a diversion. Then, running `tree -a` would give you the commit hashes in the objects directory.

Running the following commands should work:

```bash
git init
git checkout 9b763e8d718f074ae2c740eab1842cd3b411432f -f  # -f flag for force checkout and 9b763e8d718f074ae2c740eab1842cd3b411432f hash as this has the file commited into the repository.
```
