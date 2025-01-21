import tkinter as tk
from tkinter import ttk

def remove_whitespace():
    input = input_textbox.get("1.0", tk.END)
    output = "".join(input.split())
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output)

root = tk.Tk()
root.title("Whitespace Remover")
root.geometry("600x500")
root.config(bg="#2e2e2e")
root.resizable(False, False)



input_label = ttk.Label(root, text="Input Text:")
input_label.pack(pady=10)

input_textbox = tk.Text(root, height=10, width=60, wrap=tk.WORD, bd=1, relief="solid")
input_textbox.pack(pady=5)

output_label = ttk.Label(root, text="Output Text:")
output_label.pack(pady=10)

output_textbox = tk.Text(root, height=10, width=60, wrap=tk.WORD, bd=1, relief="solid")
output_textbox.pack(pady=5)

remove_button = ttk.Button(root, text="Remove Whitespace", command=remove_whitespace)
remove_button.pack(pady=20)

root.mainloop()
