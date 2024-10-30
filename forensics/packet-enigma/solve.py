import os

def decrypt(ciphertext, key):
    # Calculate the number of columns and the number of rows
    num_cols = key
    num_rows = len(ciphertext) // num_cols

    # Handle the case where padding was added
    if len(ciphertext) % num_cols != 0:
        num_rows += 1

    # Create a list to hold the characters in the correct order
    plaintext = [''] * (num_rows * num_cols)

    # Fill the plaintext array with characters from the ciphertext
    pointer = 0
    for col in range(num_cols):
        for row in range(num_rows):
            if pointer < len(ciphertext):
                plaintext[row * num_cols + col] = ciphertext[pointer]
                pointer += 1

    # Join the list to get the decrypted message
    decrypted_message = ''.join(plaintext)

    # Remove padding (if any)
    decrypted_message = decrypted_message.rstrip('*')  # Change '*' to the correct padding if needed

    return decrypted_message.strip()  # Strip whitespace

if __name__ == "__main__":
    # Get the encrypted message from the file
    with open('enc.txt', 'r') as file:
        encrypted_message = file.read().strip()  # Strip any extra whitespace/newlines

    # Try different keys
    for key in range(1, 35):
        # Decrypt the message
        decrypted_message = decrypt(encrypted_message, key)
        if "tyroCTF" in decrypted_message:
            print(f"Key {key}: Decrypted message: {decrypted_message}")
