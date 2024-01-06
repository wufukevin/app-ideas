import tkinter as tk


class BaseApp:
    def __init__(self, parent_frame, return_callback):
        self.parent_frame = parent_frame
        self.return_callback = return_callback
        self.create_widgets()

    def create_widgets(self):
        # Return to Homepage Button
        self.return_button = tk.Button(
            self.parent_frame, text="Return", command=self.return_callback)
        self.return_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        return None
