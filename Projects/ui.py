import tkinter as tk
class BaseUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Main App")
        self.parent_frame = tk.Frame(self.root)
        self.parent_frame.pack(side=tk.RIGHT, padx=0)
        self.create_widgets()

    def create_widgets(self):
        return None