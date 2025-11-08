from pathlib import Path
import random
import string
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Python\Projects\GUI Password Generator\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("400x350")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 350,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    400.0,
    350.0,
    fill="#F3F3F3",
    outline="")

canvas.create_text(
    74.0,
    14.0,
    anchor="nw",
    text="Password Generator",
    fill="#000000",
    font=("Inter ExtraBold", 25 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    164.5,
    125.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#6E6868",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=14.0,
    y=104.0,
    width=301.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    349.0,
    125.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#6E6868",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=318.0,
    y=104.0,
    width=62.0,
    height=41.0
)
FinalLabel = Label(
    text="Welcome to Password Generator",
    font=("Inter", 15 * -1)
)
FinalLabel.place(
    x=90.0,
    y=166.0,
)

def GeneratePassword():
    entry_1.delete(0, 15)
    PasswordLimit = int(entry_2.get())
    if PasswordLimit <= 15:
        Password = "".join(random.choices(string.hexdigits, k=PasswordLimit))
        FinalPassword = str(Password)
        entry_1.insert(1, FinalPassword)
        FinalLabel.config(text="Collect Your Password", fg="green")
    else:
        FinalLabel.config(text="Password can't be longer then\n15 Characters", fg="red")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=GeneratePassword,
    relief="flat"
)
button_1.place(
    x=140.0,
    y=203.0,
    width=100.0,
    height=100.0
)
window.resizable(False, False)
window.mainloop()

