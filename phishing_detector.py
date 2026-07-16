import tkinter as tk
from tkinter import messagebox

# Import your phishing detection function
# Replace with your actual file and function name
from phishing_detector import analyze_message


def analyze():
    message = text_box.get("1.0", tk.END).strip()

    if not message:
        messagebox.showwarning("Warning", "Please enter a message!")
        return

    result = analyze_message(message)

    output.config(state="normal")
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    output.config(state="disabled")


root = tk.Tk()
root.title("Phishing Awareness Checker")
root.geometry("700x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Phishing Awareness Detector",
    font=("Arial", 18, "bold"),
)
title.pack(pady=10)

label = tk.Label(root, text="Enter Email / SMS Message")
label.pack()

text_box = tk.Text(root, height=12, width=75)
text_box.pack(pady=10)

analyze_btn = tk.Button(
    root,
    text="Analyze Message",
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    command=analyze
)
analyze_btn.pack(pady=10)

tk.Label(root, text="Result").pack()

output = tk.Text(root, height=8, width=75, state="disabled")
output.pack(pady=10)

root.mainloop()