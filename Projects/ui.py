import tkinter as tk


class BaseApp:
    def __init__(self, parent_frame, return_callback, height):
        self.parent_frame = parent_frame
        self.return_callback = return_callback

        self.height = height

        self.create_widgets()

    def create_widgets(self):
        # Return to Homepage Button
        self.return_button = tk.Button(
            self.parent_frame, text="Return to Homepage", command=self.return_callback)
        # self.return_button.pack(pady=10)
        print(f"height: {self.height}")
        self.return_button.place(x=0, y=self.height)
        return None
