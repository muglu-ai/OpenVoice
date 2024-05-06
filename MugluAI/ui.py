import tkinter as tk
from tkinter import messagebox
import os

def shutdown_computer():
    # Write Python code to shutdown the computer to a file
    with open("shutdown.py", "w") as file:
        file.write("import os\nos.system('shutdown /s /t 1')")

    # Execute the shutdown code
    os.system("python shutdown.py")

# Create main application window
root = tk.Tk()
root.title("Computer Control")
root.geometry("300x150")

# Function to handle shutdown button click
def on_shutdown_click():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to shutdown your computer?")
    if confirmation:
        shutdown_computer()

# Create UI elements
label = tk.Label(root, text="Click the button to shutdown your computer:")
label.pack(pady=10)

shutdown_button = tk.Button(root, text="Shutdown", command=on_shutdown_click)
shutdown_button.pack(pady=5)

# Run the application
root.mainloop()
