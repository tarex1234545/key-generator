import tkinter as tk
import secrets
import string

# Function to generate a secure numeric key
def generate_key():
    key_length = 8  # Fixed key length of 8 digits
    
    # Generate a random numeric key
    key = ''.join(secrets.choice(string.digits) for _ in range(key_length))
    
    # Display the generated key
    keys_label.config(text=f"Generated Key: {key}")

# Function to clear the generated key
def clear_key():
    keys_label.config(text="Generated Key: ")

# Create the main application window
root = tk.Tk()
root.title("Advanced Temporary Key Generator")
root.geometry("600x450")
root.configure(bg="#1A1A1A")

# Title label
title_label = tk.Label(
    root,
    text="Temporary Key Generator",
    font=("Arial", 24, "bold"),
    fg="#FFFFFF",
    bg="#1A1A1A",
)
title_label.pack(pady=20)

# Generate key button
generate_button = tk.Button(
    root,
    text="Generate Key",
    command=generate_key,
    font=("Arial", 16),
    fg="#FFFFFF",
    bg="#008000",
    activebackground="#006400",
    relief="groove",
    width=20,
    pady=5,
)
generate_button.pack(pady=20)

# Label to display the generated key
keys_label = tk.Label(
    root,
    text="Generated Key: ",
    font=("Arial", 14),
    fg="#FFFFFF",
    bg="#1A1A1A",
    justify="left",
)
keys_label.pack(pady=20)

# Clear button to reset the output
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_key,
    font=("Arial", 16),
    fg="#FFFFFF",
    bg="#FF0000",
    activebackground="#CC0000",
    relief="groove",
    width=20,
    pady=5,
)
clear_button.pack(pady=10)

# Footer label
footer_label = tk.Label(
    root,
    text="Powered by KeyGenApp",
    font=("Arial", 12, "italic"),
    fg="#808080",
    bg="#1A1A1A",
)
footer_label.pack(side="bottom", pady=20)

# Start the Tkinter main loop
root.mainloop()
