# Solution

> [!NOTE]
>
> This question is slightly tricky and somewhat guessy.

The code is divided into two parts:

```python
funny_list = [''] * n
a = None
b = 0

for i, j in enumerate(flag):
    funny_list[b] += j
    b += 1 if b == 0 or (b < n - 1 and (i // (n - 1)) % 2 == 0) else -1

fun = ' '.join(funny_list)
```

and

```python
gem = gem.encode()
fun_bytes = fun.encode()

big_gem = (gem * (len(fun_bytes) // len(gem) + 1))[:len(fun_bytes)]

xored = bytes(a ^ b for a, b in zip(fun_bytes, big_gem))
```

Focusing on the first part, we realise that the $\text{flag size} = \text{output string size} - n + 1$

Also, the first part is famously called as a [Rail fence cipher](https://en.wikipedia.org/wiki/Rail_fence_cipher).

The guessy part here is to guess n. Clearly, $n \neq 1$. Now, we start trying at $n = 2$ (which won't work 🙃). I will show the procedure for $n = 3$ (As $n = 3$ is what I have taken, and mostly n = 3 or 4 in Rail-fence ciphers)...

As we know $n = 3$, we know the length of the flag is $36 - 3 + 1 = 34$. Now, our flag looks something like `flag = 'tyroCTF{xxxxxxxxxxxxxxxxxxxxxxxxx}'` (25 unknown chars).

Now, running the railroad on our flag:

```python
flag = 'tyroCTF{xxxxxxxxxxxxxxxxxxxxxxxxx}'
n = 3


funny_list = [''] * n
a = None
b = 0

for i, j in enumerate(flag):
    funny_list[b] += j
    b += 1 if b == 0 or (b < n - 1 and (i // (n - 1)) % 2 == 0) else -1

fun = ' '.join(funny_list)

print(fun)
```

Output:

```plaintext
tCxxxxxxx yoT{xxxxxxxxxxxx} rFxxxxxx
```

Now, we know

```plaintext
fun[0:2] = 'tC'
fun[9:14] = ' yoT{'
fun[26:30] = '} rF'
```

Now, on xorring the output string back with the original flag and comparing the known Indices, we may get some info. So, we run

```python
fun_bytes = 'tCxxxxxxx yoT{xxxxxxxxxxxx} rFxxxxxx'.encode()
xored_output = b'9,C\x17W~_\x17\x02G4\x00&\x1a8}\\\x1f\x13\x0f)\x17\x00\x03\x06+\x12R\x13!!0\x02>8y'
xored = bytes(a ^ b for a, b in zip(fun_bytes, xored_output))

print(xored)

decoded_output = ''.join(chr(c) for c in xored)
for i, c in enumerate(decoded_output):
    print(f'Index {i}: {c}')
```

Output:

```plaintext
b"Mo;o/\x06'ozgMora@\x05$gkwQox{~SoragYHzF@\x01"
Index 0: M
Index 1: o
Index 2: ;
Index 3: o
Index 4: /
Index 5:
Index 6: '
Index 7: o
Index 8: z
Index 9: g
Index 10: M
Index 11: o
Index 12: r
Index 13: a
Index 14: @
Index 15:
Index 16: $
Index 17: g
Index 18: k
Index 19: w
Index 20: Q
Index 21: o
Index 22: x
Index 23: {
Index 24: ~
Index 25: S
Index 26: o
Index 27: r
Index 28: a
Index 29: g
Index 30: Y
Index 31: H
Index 32: z
Index 33: F
Index 34: @
Index 35:
```

Focusing on the relevant info:

```plaintext
fun[0:2] = 'tC'
fun[9:14] = ' yoT{'
fun[26:30] = '} rF'
b"Mo;o/\x06'ozgMora@\x05$gkwQox{~SoragYHzF@\x01"
Index 0: M
Index 1: o
...
Index 9: g
Index 10: M
Index 11: o
Index 12: r
Index 13: a
...
Index 26: o
Index 27: r
Index 28: a
Index 29: g
...

big_gem = 'Mo...gMora...orag...'
```

On simple observation and using the fact that `big_gem` is the string `gem` repeating,

```plaintext
big_gem = b'MoragMoragMoragMoragMoragMoragMoragM'
gem = 'Morag'
```

Now, we have all the data.

```python
xored = b'9,C\x17W~_\x17\x02G4\x00&\x1a8}\\\x1f\x13\x0f)\x17\x00\x03\x06+\x12R\x13!!0\x02>8y'
gem = 'Morag'
n = 3

gem = gem.encode()
big_gem = (gem * (len(xored) // len(gem) + 1))[:len(xored)]
fun_bytes = bytes(a ^ b for a, b in zip(xored, big_gem))
fun = fun_bytes.decode()

funny_list = fun.split()

block_lengths = [len(block) for block in funny_list]
total_length = sum(block_lengths)

zigzag_pattern = [''] * total_length
rail_indexes = [0] * n
pos = 0
direction = 1

for i in range(total_length):
    zigzag_pattern[i] = funny_list[pos][rail_indexes[pos]]
    rail_indexes[pos] += 1

    if pos == 0:
        direction = 1
    elif pos == n - 1:
        direction = -1
    pos += direction

flag = ''.join(zigzag_pattern)
print(flag)
```

We get the flag as: **`tyroCTF{1_l0v3_m0rph3d_x0r_bea4fc}`**
