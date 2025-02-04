from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None

# Function to create a new file
def newFile(text):
    global filename
    updateFilename("Untitled")
    text.delete(0.0, END)  # Clear the text widget

# Function to save the current file
def saveFile(text, label):
    global filename
    if filename == "Untitled": 
        saveAs(text, label)
    t = text.get(0.0, END)  # Get all text from the text widget
    f = open(filename, 'w')  # Open the file in write mode
    f.write(t)  # Write the text to the file
    f.close()  # Close the file

# Function to save the file with a new name
def saveAs(text, label):
    f = asksaveasfile(mode='w', defaultextension='.txt')  # Open save as dialog
    t = text.get(0.0, END)  # Get all text from the text widget
    try:
        f.write(t.rstrip())  # Write the text to the file, removing trailing whitespace
        if isinstance(label, Label):
            updateFilename(f.name)
            label.configure(text=currentFilename())
    except:
        showerror(title="Oops!", message="Unable to save file...")  # Show error if save fails

# Function to open an existing file
def openFile(text, label):
    f = askopenfile(mode='r')  # Open file dialog
    t = f.read()  # Read the file content
    if isinstance(label, Label):
        updateFilename(f.name)
        label.configure(text=currentFilename())
    text.delete(0.0, END)  # Clear the text widget
    text.insert(0.0, t)  # Insert the file content into the text widget
    
def currentFilename():
    return filename

def updateFilename(string):
    global filename
    filename = string