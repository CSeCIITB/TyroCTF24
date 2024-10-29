import time

from pwn import *

# Path to the executable 'chall'
chall_path = "./chall"

# Input string for the challenge


# Function to measure the execution time
def measure_execution_time(input_str):
    # Start the timer
    start_time = time.time()

    # Run the process with the given input
    p = process(chall_path)

    # Send the input to the process
    p.sendline(input_str)

    # Wait for the process to complete
    p.recvall()

    # Stop the timer
    end_time = time.time()

    # Calculate the execution time
    exec_time = end_time - start_time

    # Return the execution time
    return exec_time


matched_string = ""
un_matched_string = ""

# Loop through all the printable charecters, take the one with the most time.
valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"
max_t0_first_iter = 0
for i in range(0, 100):
    max_time = 0
    toadd_char = ""
    for c in valid_chars:
        input_str = un_matched_string + c
        exec_time = measure_execution_time(input_str)
        if exec_time > max_time:
            max_time = exec_time
            toadd_char = c
    matched_string += toadd_char
    if toadd_char == "}":
        un_matched_string += "a"
    else:
        un_matched_string += "}"

    import sys

    if i == 0:
        max_t0_first_iter = max_time
    else:
        if max_time < max_t0_first_iter / 2:
            break
    print(matched_string, file=sys.stderr)
