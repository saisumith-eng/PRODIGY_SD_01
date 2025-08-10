import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Main function to convert temperature
def convert_temp():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            f = celsius_to_fahrenheit(temp)
            k = celsius_to_kelvin(temp)
            result_label.config(text=f"{temp}°C = {f:.2f}°F\n{temp}°C = {k:.2f}K")

        elif unit == "Fahrenheit":
            c = fahrenheit_to_celsius(temp)
            k = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"{temp}°F = {c:.2f}°C\n{temp}°F = {k:.2f}K")

        elif unit == "Kelvin":
            c = kelvin_to_celsius(temp)
            f = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"{temp}K = {c:.2f}°C\n{temp}K = {f:.2f}°F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Tkinter Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
#root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Temperature Input
entry_temp = tk.Entry(root, font=("Arial", 12))
entry_temp.pack(pady=5)

# Unit Selection
unit_var = tk.StringVar()
unit_choices = ["Celsius", "Fahrenheit", "Kelvin"]
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=unit_choices, font=("Arial", 12), state="readonly")
unit_menu.pack(pady=5)
unit_menu.current(0)

# Convert Button
convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_temp)
convert_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
