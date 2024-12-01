import tkinter as tk
from tkinter import messagebox

# Caesar Cipher encryption function
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char.upper()) - 65 + shift_amount) % 26 + 65)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

# Caesar Cipher decryption function
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Function to handle encryption button click
def encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = caesar_encrypt(text, shift)
    result_text.set(f"Encrypted Text: {encrypted_text}")

# Function to handle decryption button click
def decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = caesar_decrypt(text, shift)
    result_text.set(f"Decrypted Text: {decrypted_text}")

# Create the main window
root = tk.Tk()
root.title("Cryptography Tool")

# Create and place the components
label_text = tk.Label(root, text="Enter Text:")
label_text.grid(row=0, column=0, padx=5, pady=5)

entry_text = tk.Entry(root, width=50)
entry_text.grid(row=0, column=1, padx=5, pady=5)

label_shift = tk.Label(root, text="Enter Shift:")
label_shift.grid(row=1, column=0, padx=5, pady=5)

entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_encrypt.grid(row=2, column=0, padx=5, pady=5)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.grid(row=2, column=1, padx=5, pady=5)

result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text)
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
