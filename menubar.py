from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

import file

def createMenuBar(root, text, label):
    menubar = Menu(root)
    fileCommands = Menu(menubar)
    createFileMenu(root, text, label, fileCommands)
    menubar.add_cascade(label="File", menu=fileCommands)  # Add the File menu to the menu bar
    return menubar

def createFileMenu(root, text, label, commands: Menu):
    commands.add_command(label="New", command=lambda: file.newFile(text))  # Add New command to the menu
    commands.add_command(label="Open", command=lambda: file.openFile(text, label))  # Add Open command to the menu
    commands.add_command(label="Save", command=lambda: file.saveFile(text, label))  # Add Save command to the menu
    commands.add_command(label="Save as...", command=lambda: file.saveAs(text, label))  # Add Save As command to the menu
    commands.add_separator()  # Add a separator
    commands.add_command(label="Quit", command=(root.quit))  # Add Quit command to the menu
