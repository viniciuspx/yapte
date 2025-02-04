from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

from menubar import createMenuBar
import file

root = Tk()
root.title("YAPTE") 
root.geometry("800x600")
root.state('zoomed')

text = Text(root, width=400, height=400, background='#222222', foreground='white', padx=20, pady=5, blockcursor=True, font='Courier 14', insertbackground='white')

file.newFile(text)

label = Label(root, text=file.currentFilename(), height=1, width=file.currentFilename().__sizeof__(), background='#222222', foreground='white')

label.pack()
text.pack()  

menubar = createMenuBar(root, text, label)

root.config(menu=menubar)
root.mainloop() 