import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Product Calculator App")
root.geometry("400x250")

tk.Label(root, text="First Number").grid(row=0, column=0, padx=10, pady=5)
num1_entry = tk.Entry(root)
num1_entry.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0, padx=10, pady=5)
num2_entry = tk.Entry(root)
num2_entry.grid(row=1, column=1)

def calculate_product():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        product = num1 * num2
        messagebox.showinfo("Result", f"Product: {product}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

tk.Button(root, text="Calculate Product", command=calculate_product).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
