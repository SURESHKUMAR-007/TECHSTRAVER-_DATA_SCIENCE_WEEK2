import tkinter as tk
from tkinter import messagebox

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{celsius:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Celsius input
label_celsius = tk.Label(window, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

entry_celsius = tk.Entry(window)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_celsius = tk.Button(window, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_celsius.grid(row=0, column=2, padx=10, pady=10)

# Fahrenheit input
label_fahrenheit = tk.Label(window, text="Fahrenheit:")
label_fahrenheit.grid(row=1, column=0, padx=10, pady=10)

entry_fahrenheit = tk.Entry(window)
entry_fahrenheit.grid(row=1, column=1, padx=10, pady=10)

button_fahrenheit = tk.Button(window, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_fahrenheit.grid(row=1, column=2, padx=10, pady=10)

# Run the application
window.mainloop()
