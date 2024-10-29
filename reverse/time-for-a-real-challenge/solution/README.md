# Solution

The binary has been compiled using [movfuscator](https://github.com/xoreaxeaxeax/movfuscator) hence it is difficult to decompile the binary.

Upon running it one may notice that certain inputs cause a significant time delay in the output. The binary performs a large number of operations on the input for each charecter that matches with the flag

So we can use this to our advantage to find the flag charecter by charecter. The script using this approach is also provided in this repository
