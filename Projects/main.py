import tkinter as tk
from tkinter import ttk
from main_app import MainApp
from main_app import Input_Class
from lv2_bit_masks import TimezoneApp
from lv2_book_finder import BookSearchApp
from lv2_calculator import CalculatorApp



root = tk.Tk()
app = MainApp(root, [Input_Class(TimezoneApp, "Timezone App"),
              Input_Class(BookSearchApp, "Book Search App"),
              Input_Class(CalculatorApp, "Calculator App"),])
root.mainloop()