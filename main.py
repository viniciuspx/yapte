from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

# Initialize the filename variable
filename = None

# Function to create a new file
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  # Clear the text widget

# Function to save the current file
def saveFile():
    global filename
    t = text.get(0.0, END)  # Get all text from the text widget
    f = open(filename, 'w')  # Open the file in write mode
    f.write(t)  # Write the text to the file
    f.close()  # Close the file

# Function to save the file with a new name
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')  # Open save as dialog
    t = text.get(0.0, END)  # Get all text from the text widget
    try:
        f.write(t.rstrip())  # Write the text to the file, removing trailing whitespace
    except:
        showerror(title="Oops!", message="Unable to save file...")  # Show error if save fails

# Function to open an existing file
def openFile():
    f = askopenfile(mode='r')  # Open file dialog
    t = f.read()  # Read the file content
    text.delete(0.0, END)  # Clear the text widget
    text.insert(0.0, t)  # Insert the file content into the text widget

# Create the main application window
root = Tk()
root.title("YAPTE")  # Set the window title
root.minsize(width=400, height=400)  # Set the minimum window size
root.maxsize(width=800, height=600)  # Set the maximum window size

# Create a text widget for text editing
text = Text(root, width=400, height=400)
text.pack()  # Add the text widget to the window

# Create a menu bar
menubar = Menu(root)
filename = Menu(menubar)
filename.add_command(label="New", command=newFile)  # Add New command to the menu
filename.add_command(label="Open", command=openFile)  # Add Open command to the menu
filename.add_command(label="Save", command=saveFile)  # Add Save command to the menu
filename.add_command(label="Save as...", command=saveAs)  # Add Save As command to the menu
filename.add_separator()  # Add a separator
filename.add_command(label="Quit", command=(root.quit))  # Add Quit command to the menu
menubar.add_cascade(label="File", menu=filename)  # Add the File menu to the menu bar

# Configure the window to display the menu bar
root.config(menu=menubar)

# Create new file, first time only
print("=> Creating new empty file")
newFile()

root.mainloop()  # Start the Tkinter event loop