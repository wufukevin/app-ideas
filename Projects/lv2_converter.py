import argparse
import random
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import subprocess
from ui import BaseApp
import os
from enum import Enum

#1. api 

class Converter(BaseApp):
    def __init__(self, header_frame, content_frame, footer_frame, return_callback):
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
            'JPY': 110.0,
            # Add more currencies and their exchange rates
        }

        # Variables
        self.amount_var = tk.StringVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()
        super().__init__(header_frame, content_frame, footer_frame, return_callback)

    def create_widgets(self):
        # Source amount entry
        amount_label = tk.Label(self.content_frame, text="Enter Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10)

        # Validate only input numbers
        amount_entry = tk.Entry(self.content_frame, textvariable=self.amount_var, validate="key", validatecommand=(
            self.content_frame.register(self.validate_amount), '%P'))
        amount_entry.grid(row=0, column=1, padx=10, pady=10)
        amount_entry.bind("<Return>", self.update_result)

        # Source currency dropdown
        from_currency_label = tk.Label(self.content_frame, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        from_currency_combobox = ttk.Combobox(
            self.content_frame, textvariable=self.from_currency_var, values=list(self.exchange_rates.keys()))
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        from_currency_combobox.bind("<<ComboboxSelected>>", self.update_result)

        # Destination currency dropdown
        to_currency_label = tk.Label(self.content_frame, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        to_currency_combobox = ttk.Combobox(
            self.content_frame, textvariable=self.to_currency_var, values=list(self.exchange_rates.keys()))
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        to_currency_combobox.bind("<<ComboboxSelected>>", self.update_result)

        # Result label
        result_label = tk.Label(self.content_frame, text="Result:")
        result_label.grid(row=3, column=0, padx=10, pady=10)

        result_entry = tk.Entry(
            self.content_frame, textvariable=self.result_var, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Change button
        convert_button = tk.Button(
            self.footer_frame, text="Change", command=self.change_currency)
        convert_button.pack(side=tk.RIGHT, pady=10)

        super().create_widgets()
        

    def validate_amount(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def change_currency(self):
        from_value = self.from_currency_var.get()
        self.from_currency_var.set(self.to_currency_var.get())
        self.to_currency_var.set(from_value)

        self.update_result()
    
    def update_result(self, event=None):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            if from_currency and to_currency:
                result = amount * \
                    (self.exchange_rates[to_currency] /
                     self.exchange_rates[from_currency])
                self.result_var.set(f"{result:.2f}")
        except ValueError:
            self.result_var.set("Invalid Input")
