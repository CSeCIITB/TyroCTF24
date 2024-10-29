c = "181c5d1a2ce0141c5a1a4a2dc4e84286d4c308d8d1dac49ce80bf2aaadb978ac4feecabb5f7e08a5166ef002f96a6477f7f423893a28b4e669597429b8c85425f39618605cffd2698ab162903e6e957b5474764490b50594056dfb3d01ce1a3df5bd5d7bea4f5117a5443a10fcdebc3191c97ccbfcad6edda68c121f991a05c237926765"

from Crypto.Util.number import long_to_bytes

c_int = int(c, 16)

# Running a binary search for cuberoot (seems tougher than it is)

i = 1
j = c_int

while i < j:
    mid = (i + j) // 2
    if mid**3 < c_int:
        i = mid + 1
    elif mid**3 > c_int:
        j = mid - 1
    else:
        print(long_to_bytes(mid))
        break
