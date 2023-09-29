import tkinter as tk
from tkinter import filedialog
import base64
import tkinter.scrolledtext as scrolledtext

def encode_file_to_base64():
    file_path = filedialog.askopenfilename(title="Select a file to encode")
    
    if file_path:
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
                encoded_data = base64.b64encode(file_data).decode("utf-8")
                result_text.config(state='normal')
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, encoded_data)
                result_text.config(state='disabled')
        except Exception as e:
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"An error occurred: {str(e)}")
            result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "No file selected.")
        result_text.config(state='disabled')

# Create a GUI window
root = tk.Tk()
root.title("Base64 Encoder")

# Create a scrolled text widget to display the result
result_text = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD, state='disabled')
result_text.pack()

# Create a button to trigger the encoding process
encode_button = tk.Button(root, text="Encode File", command=encode_file_to_base64)
encode_button.pack()

# Close the GUI window (optional)
root.mainloop()