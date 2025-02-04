import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

from menubar import create_menu_bar
import file

def main():
    root = tk.Tk()
    root.title("YAPTE")
    root.geometry("800x600")
    root.state('zoomed')

    text_widget = tk.Text(root, width=400, height=400, background='#222222', foreground='white', padx=20, pady=5, blockcursor=True, font='Courier 14', insertbackground='white')

    file.new_file(text_widget)

    filename_label = tk.Label(root, text=file.current_filename(), height=1, width=file.current_filename().__sizeof__(), background='#222222', foreground='white')

    filename_label.pack()
    text_widget.pack()

    menubar = create_menu_bar(root, text_widget, filename_label)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()