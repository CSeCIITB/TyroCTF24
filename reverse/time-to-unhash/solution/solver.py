from pwn import *

path_binary = "./a.out"

p = process(path_binary)
a1 = p.recvline()
a2 = p.recvline()[0:-1]
a2_1 = a2.decode('utf-8')
a3 = p.recvuntil(b":")
p.sendline(b"1")
a4 = p.recvline()
a5 = p.recvuntil(b":")
a6 = int(p.recvline()[:-1].decode('utf-8'))

p.close()
# sleep(0)
# print(a1)
# print(a2)
# print(a2_1)
# print(a3)
# print(a4)
# print(a5)
# print(a6)


p2 = process(path_binary)
a1 = p2.recvline()
a2 = p2.recvline()
a3 = p2.recvuntil(b":")
p2.sendline(str(a6).encode('utf-8'))
a5 = p2.recvline()
a6 = p2.recvline()




p2.close()





print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

