import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from functions import * 
import os

def main():
    ensure_file()

#window parameters
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("500x500")
    root.resizable(False,False)
    tk.Label(root, text = "To-Do List").grid(row=0, column=0, columnspan=2, pady=10)

#creating and placing buttons
    tk.Button(root, text="Add", command= lambda: create_task(root, message_box)).grid(row=2, column=0, pady=10)
    tk.Button(root, text="Complete", command= lambda: complete_task(message_box)).grid(row=2, column=1, pady=10)
    

#creating the message box where the to-do list will be displayed
    message_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width= 60, height= 20)
    message_box.grid(row=1, column=0, columnspan=2)
    message_box.config(state=tk.DISABLED)

    refresh_list(message_box)



    root.mainloop()

if __name__ == "__main__":
    main()