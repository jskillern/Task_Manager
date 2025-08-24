import tkinter as tk
from tkinter import ttk
from functions import *  


def main():
      


#window parameters
    root = tk.Tk()
    root.minsize(250, 100)
    root.maxsize(500, 800)
    root.geometry("500x500")
    tk.Label(root, text = "To-Do List").grid()

#creating buttons
    add = tk.Button(root, text="Add", command = add_task)
    add.grid(row=1, column=0)
    
    complete = tk.Button(root, text="Complete", command = complete_task)
    complete.grid(row=1, column=1)








    root.mainloop()

if __name__ == "__main__":
    main()