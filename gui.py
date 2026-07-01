from logic import count_words
import tkinter as tk

root = tk.Tk()

text_input = tk.Text(root, height=10, width=50)
text_input.pack()

result_label = tk.Label(root, text="Words: 0")
result_label.pack()

def on_click():
    text = text_input.get("1.0", "end-1c").strip()
    count = count_words(text)
    result_label.config(text=f"Words: {count}")

button = tk.Button(root, text="Count Words", command=on_click)
button.pack()

root.mainloop()