## Lazy Calc

| Author | Difficulty | Points | Solves | First Blood    |
| ------ | ---------- | ------ | ------ | -------------- |
| RatanKokal and Sam-MARTis  | Easy   | 330    | 18     | kugelblitz |

---

### Description

<blockquote>
Ughh, my prof wants me to make a calculator website using python.
I'm too lazy to make all those operations work.
Why reinvent the wheel? Surely I could make python do the calculation directly...
After all, what could go wrong!

# Deploying container on local system

To deploy the system on your localhost, run the following command.

```
docker build -t tyroctf .
docker run -d -p 1337:1337 tyroctf
```

After deploying the container you can access it by running this command.

```
nc localhost 1337
```

## Aliter

Alternatively, you can simply take a look at the `chall.pyc` file and not worry about other files. Do note that the flag's path is hardcoded as an absolute one with respect to the container so you would get an error even with a `flag.txt` file in the CWD.
