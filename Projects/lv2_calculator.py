import argparse
import tkinter as tk
from tkinter import messagebox
import subprocess
from ui import BaseApp

class CalculatorApp(BaseApp):
    def __init__(self, parent_frame, return_callback):
        super().__init__(parent_frame, return_callback)

    def create_widgets(self):
        # Entry widget to input numbers
        self.num_entry = tk.Entry(self.parent_frame)
        self.num_entry.pack(pady=5)
        self.search_button = tk.Button(
            self.parent_frame, text="Enter", command=self.enter_click)
        self.search_button.pack(pady=10)

    def enter_click(self):
        current_text = self.num_entry.get()
        try:
            result = subprocess.check_output(
                ["python3", "Projects/lv2_calculator.py", *current_text.split()]).decode("utf-8")
            messagebox.showinfo("Result", f"Result: {result}")
            self.num_entry.delete(0, tk.END)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error: {e.output}")

def add_numbers(numbers):
    return sum(numbers)


def add_float_numbers(numbers):
    return sum(map(float, numbers))


def add_even_numbers(numbers):
    return sum([int(num) for num in numbers if int(num) % 2 == 0])


def add_odd_numbers(numbers):
    return sum([int(num) for num in numbers if int(num) % 2 != 0])


def main():
    parser = argparse.ArgumentParser(description='Calculator CLI')

    parser.add_argument('numbers', metavar='N', type=float,
                        nargs='+', help='Numbers to be added')
    parser.add_argument('-f', '--float', action='store_true',
                        help='Add floating-point numbers')
    parser.add_argument('--even', action='store_true',
                        help='Add only even numbers')
    parser.add_argument('--odd', action='store_true',
                        help='Add only odd numbers')

    args = parser.parse_args()

    if args.even and args.odd:
        print("Error: Cannot use --even and --odd flags simultaneously.")
        return

    result = 0

    if args.float:
        result = add_float_numbers(args.numbers)
    elif args.even:
        result = add_even_numbers(args.numbers)
    elif args.odd:
        result = add_odd_numbers(args.numbers)
    else:
        result = add_numbers(args.numbers)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
