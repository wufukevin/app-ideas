import tkinter as tk


class BaseApp:
    def __init__(self, header_frame, content_frame, footer_frame, return_callback):
        self.header_frame = header_frame
        self.content_frame = content_frame
        self.footer_frame = footer_frame
        self.return_callback = return_callback
        self.create_widgets()

    def create_widgets(self):
        # Return to Homepage Button
        self.return_button = tk.Button(
            self.footer_frame, text="Return", command=self.return_callback)
        self.return_button.pack(side=tk.BOTTOM, pady=10)
        return None
