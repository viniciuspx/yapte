from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename: str = "Untitled"

def new_file(text: Text) -> None:
    global filename
    update_filename("Untitled")
    text.delete(0.0, END)

def save_file(text: Text, label: Label) -> None:
    global filename
    if filename == "Untitled":
        save_as(text, label)
    else:
        with open(filename, 'w') as f:
            f.write(text.get(0.0, END))

def save_as(text: Text, label: Label) -> None:
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    try:
        f.write(text.get(0.0, END).rstrip())
        update_filename(f.name)
        label.configure(text=current_filename())
    except Exception as e:
        showerror(title="Oops!", message=f"Unable to save file: {e}")
    finally:
        f.close()

def open_file(text: Text, label: Label) -> None:
    f = askopenfile(mode='r')
    if f is None:
        return
    try:
        t = f.read()
        update_filename(f.name)
        label.configure(text=current_filename())
        text.delete(0.0, END)
        text.insert(0.0, t)
    except Exception as e:
        showerror(title="Oops!", message=f"Unable to open file: {e}")
    finally:
        f.close()

def current_filename() -> str:
    return filename

def update_filename(string: str) -> None:
    global filename
    filename = string
