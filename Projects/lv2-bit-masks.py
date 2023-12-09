from tkinter import *
from tkinter import ttk

gmt = {
    "Moscow": 3,
    "Paris": 2,
    "Berlin": 2,
    "Brussels": 2,
    "Amsterdam": 2,
    "Rome": 2,
    "London": 1,
    "Dublin": 1,
    "New York": -4,
    "Washington": -4,
    "St. Louis": -5,
    "Los Angeles": -7,
    "Tokyo": 9,
    "Beijing": 8,
    "Ho Chi Mihn City": 7,
    "Mumbai": 5,
}

def showGMT(place: tuple):
    sign = "+" if place[1]>0 else ""
    return f"{place[0]}: GMT {sign}{place[1]}"

def changTitle():
    input_gmt = input_entry.get()
    input_entry.delete(0, 'end')
    for place in gmt.items():
        if place[1] == int(input_gmt):
            label.config(text=showGMT(place))
            return
    label.config(text="Find no answer~~")

root = Tk()
root.geometry("300x800")
title = "Find Result!"
label = ttk.Label(root, text=title)
label.pack()
input_entry = ttk.Entry(root, width=30)
input_entry.pack()
ttk.Button(root, text="Find Cities", command=changTitle).pack()
ttk.Button(root, text="Quit", command=root.destroy).pack()

for place in gmt.items():
    Label(text=showGMT(place), font=("Arial", 14, "bold"),
                  padx=5, pady=5, bg="white", fg="black", anchor='w', justify='left').pack(fill='x')

root.mainloop()
