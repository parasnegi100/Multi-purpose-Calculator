import tkinter as tk
from tkinter import ttk, messagebox
import math

APP_FONT = ("Segoe UI", 10)
HEADER_FONT = ("Segoe UI", 14, "bold")


# ---------------- Basic Calculator ----------------
class BasicCalculator(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.geometry("300x400")

        self.entry = tk.Entry(self, font=HEADER_FONT, justify="right")
        self.entry.pack(fill="both", padx=10, pady=10, ipady=5)

        btns = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        frame = tk.Frame(self)
        frame.pack()

        for (text, row, col) in btns:
            tk.Button(frame, text=text, width=5, height=2,
                      command=lambda t=text: self.on_click(t)).grid(row=row, column=col, padx=5, pady=5)

    def on_click(self, char):
        if char == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, char)


# ---------------- Scientific Calculator ----------------
class ScientificCalculator(BasicCalculator):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        sci_btns = [
            ('sin', math.sin), ('cos', math.cos), ('tan', math.tan),
            ('sqrt', math.sqrt), ('log', math.log), ('pi', lambda: math.pi)
        ]

        sci_frame = tk.Frame(self)
        sci_frame.pack()

        for (text, func) in sci_btns:
            tk.Button(sci_frame, text=text, width=7,
                      command=lambda f=func: self.apply_func(f)).pack(side="left", padx=3, pady=3)

    def apply_func(self, func):
        try:
            value = float(self.entry.get())
            result = func(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except:
            messagebox.showerror("Error", "Invalid Input")


# ---------------- BMI Calculator ----------------
class BMICalculator(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("BMI Calculator")
        self.geometry("300x200")

        tk.Label(self, text="Weight (kg):").pack(pady=5)
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        tk.Label(self, text="Height (m):").pack(pady=5)
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        tk.Button(self, text="Calculate", command=self.calculate_bmi).pack(pady=10)

    def calculate_bmi(self):
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
            bmi = w / (h ** 2)
            messagebox.showinfo("Result", f"Your BMI is {bmi:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input")


# ---------------- Calorie Calculator ----------------
class CalorieCalculator(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Calorie Calculator")
        self.geometry("300x250")

        tk.Label(self, text="Weight (kg):").pack()
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack()

        tk.Label(self, text="Height (cm):").pack()
        self.height_entry = tk.Entry(self)
        self.height_entry.pack()

        tk.Label(self, text="Age:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Gender (M/F):").pack()
        self.gender_entry = tk.Entry(self)
        self.gender_entry.pack()

        tk.Button(self, text="Calculate", command=self.calculate_calories).pack(pady=10)

    def calculate_calories(self):
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
            age = int(self.age_entry.get())
            gender = self.gender_entry.get().strip().upper()

            if gender == 'M':
                bmr = 88.362 + (13.397 * w) + (4.799 * h) - (5.677 * age)
            elif gender == 'F':
                bmr = 447.593 + (9.247 * w) + (3.098 * h) - (4.330 * age)
            else:
                raise ValueError

            messagebox.showinfo("Result", f"Your BMR is {bmr:.2f} calories/day")
        except:
            messagebox.showerror("Error", "Invalid Input")


# ---------------- Unit Converter ----------------
class UnitConverter(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("300x200")

        self.value_entry = tk.Entry(self)
        self.value_entry.pack(pady=5)

        self.unit_var = tk.StringVar(value="km_to_miles")
        options = [
            ("Km to Miles", "km_to_miles"),
            ("Miles to Km", "miles_to_km"),
            ("Kg to Pounds", "kg_to_pounds"),
            ("Pounds to Kg", "pounds_to_kg")
        ]

        for text, mode in options:
            tk.Radiobutton(self, text=text, variable=self.unit_var, value=mode).pack(anchor="w")

        tk.Button(self, text="Convert", command=self.convert).pack(pady=10)

    def convert(self):
        try:
            val = float(self.value_entry.get())
            mode = self.unit_var.get()

            if mode == "km_to_miles":
                res = val * 0.621371
            elif mode == "miles_to_km":
                res = val / 0.621371
            elif mode == "kg_to_pounds":
                res = val * 2.20462
            elif mode == "pounds_to_kg":
                res = val / 2.20462
            else:
                res = None

            if res is not None:
                messagebox.showinfo("Result", f"Converted value: {res:.2f}")
        except:
            messagebox.showerror("Error", "Invalid Input")


# ---------------- Main Menu ----------------
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Purpose Calculator")
        self.geometry("300x300")

        tk.Label(self, text="Select a Calculator", font=HEADER_FONT).pack(pady=10)

        tk.Button(self, text="Basic Calculator", width=20, command=BasicCalculator).pack(pady=5)
        tk.Button(self, text="Scientific Calculator", width=20, command=ScientificCalculator).pack(pady=5)
        tk.Button(self, text="BMI Calculator", width=20, command=BMICalculator).pack(pady=5)
        tk.Button(self, text="Calorie Calculator", width=20, command=CalorieCalculator).pack(pady=5)
        tk.Button(self, text="Unit Converter", width=20, command=UnitConverter).pack(pady=5)


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()