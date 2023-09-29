import tkinter as tk
from tkinter import filedialog
import base64

def decode_base64_and_display():
    encoded_data = input_text.get("1.0", "end-1c")
    if encoded_data:
        try:
            decoded_data = base64.b64decode(encoded_data.encode("utf-8"))
            
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, decoded_data.decode("utf-8"))
            result_text.config(state='disabled')
        except Exception as e:
            result_text.config(state='normal')
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"An error occurred: {str(e)}")
            result_text.config(state='disabled')
    else:
        result_text.config(state='normal')
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "No data to decode.")
        result_text.config(state='disabled')

def save_decoded_data():
    decoded_data = result_text.get("1.0", "end-1c")
    if decoded_data:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Save Decoded Data")
        
        if save_path:
            with open(save_path, "w") as file:
                file.write(decoded_data)
            
            print(f"Decoded data saved to: {save_path}")
        else:
            print("Saving canceled.")

# Create a GUI window
root = tk.Tk()
root.title("Base64 Decoder")

# Create a text widget to input Base64-encoded data
input_text = tk.Text(root, width=50, height=10, wrap=tk.WORD)
input_text.pack()

# Create a button to trigger the decoding process
decode_button = tk.Button(root, text="Decode", command=decode_base64_and_display)
decode_button.pack()

# Create a Text widget to display the decoded data with a scrollbar
result_text = tk.Text(root, width=50, height=10, wrap=tk.WORD, state='disabled')
result_text.pack()

# Create a scrollbar for the result_text widget
scrollbar = tk.Scrollbar(root, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

# Create a button to save the decoded data
save_button = tk.Button(root, text="Save Decoded Data", command=save_decoded_data)
save_button.pack()

# Close the GUI window (optional)
root.mainloop()
