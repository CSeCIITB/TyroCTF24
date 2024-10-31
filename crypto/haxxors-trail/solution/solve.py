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
