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
</blockquote>

### Deploying container on local system

To deploy the system on your localhost, run the following command.

```
docker build -t tyroctf .
docker run -d -p 8000:8000 tyroctf
```

After deploying the container you can access it by running this command.

[Click here to access the app](http://0.0.0.0:8000/)

