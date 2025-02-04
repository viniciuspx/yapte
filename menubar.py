import tkinter as tk
import file

def create_menu_bar(root, text_widget, status_label):
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar)
    create_file_menu(root, text_widget, status_label, file_menu)
    menubar.add_cascade(label="File", menu=file_menu)
    return menubar

def create_file_menu(root, text_widget, status_label, menu: tk.Menu):
    menu.add_command(label="New", command=lambda: file.new_file(text_widget))
    menu.add_command(label="Open", command=lambda: file.open_file(text_widget, status_label))
    menu.add_command(label="Save", command=lambda: file.save_file(text_widget, status_label))
    menu.add_command(label="Save as...", command=lambda: file.save_as(text_widget, status_label))
    menu.add_separator()
    menu.add_command(label="Quit", command=root.destroy)
