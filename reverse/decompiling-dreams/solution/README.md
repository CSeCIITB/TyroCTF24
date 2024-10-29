# Solution

A basic decompilation of the file using [dogbolt decompiler](https://dogbolt.org/) for example. Will reveal the code

Now realise that an even number of XOR operations will result in the original value. So the inner for loops (which take up a lot of time) do not change the value of the flag. So we can just remove them and write a new script to get the flag.
