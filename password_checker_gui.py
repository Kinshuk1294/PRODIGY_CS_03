import tkinter as tk
from tkinter import messagebox
import re

# Function to evaluate password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters required")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Add number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add special character")

    if score == 5:
        return "✅ Very Strong", "#00c853", []
    elif score == 4:
        return "✅ Strong", "#2962ff", feedback
    elif score == 3:
        return "🟡 Moderate", "#ffab00", feedback
    else:
        return "🔴 Weak", "#d50000", feedback

# Function called on button click
def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, color, feedback = check_password_strength(password)
    result_label.config(text=strength, fg=color)

    suggestions_list.delete(0, tk.END)
    for item in feedback:
        suggestions_list.insert(tk.END, item)

# Set up GUI window
window = tk.Tk()
window.title("🔐 Password Strength Checker")
window.geometry("500x400")
window.config(bg="#f0f4f8")
window.resizable(False, False)

# Title
tk.Label(window, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

# Frame for input
frame = tk.Frame(window, bg="white", bd=2, relief="groove")
frame.pack(pady=10, padx=20, fill="both", expand=False)

# Entry and label
tk.Label(frame, text="Enter Password:", font=("Helvetica", 12), bg="white", fg="#333").pack(pady=(10, 0))
entry = tk.Entry(frame, show="*", font=("Helvetica", 12), width=30, bd=2, relief="solid")
entry.pack(pady=5)

# Button
tk.Button(frame, text="Check Strength", command=on_check, font=("Helvetica", 12, "bold"),
          bg="#6200ea", fg="white", activebackground="#7c4dff").pack(pady=10)

# Result label
result_label = tk.Label(frame, text="", font=("Helvetica", 14, "bold"), bg="white")
result_label.pack()

# Suggestions
tk.Label(window, text="Suggestions to improve:", font=("Helvetica", 12, "italic"), bg="#f0f4f8", fg="#444").pack(pady=(10, 0))
suggestions_list = tk.Listbox(window, font=("Helvetica", 10), height=5, width=60, bd=2, relief="solid")
suggestions_list.pack(pady=5)

# Run the GUI loop
window.mainloop()
