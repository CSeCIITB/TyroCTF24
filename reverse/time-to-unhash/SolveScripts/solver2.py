from hashlib import sha256
from pwn import *

dictNums = {}
for i in range(1000000):
    dictNums[sha256(str(i).encode()).hexdigest()] = i
    



path_binary = "./a.out"

p = process(path_binary)
a1 = p.recvline()
a2 = p.recvline()[0:-1]
a2_1 = a2.decode('utf-8')
a3 = p.recvuntil(b":")
p.sendline(str(dictNums[a2_1]).encode('utf-8'))
a4 = p.recvline()
a5 = p.recvline()

p.close()

print(a5)

# print(sha256(str(209868).encode()).hexdigest())
# print('Done')
