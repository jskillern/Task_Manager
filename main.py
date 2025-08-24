import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from functions import *  


def main():
      


#window parameters
    root = tk.Tk()
    root.minsize(500, 500)
    root.maxsize(500, 500)
    root.geometry("500x500")
    tk.Label(root, text = "To-Do List").grid(row=0, column=4, columnspan=4)

#creating and placing buttons
    add = tk.Button(root, text="Add", command = add_task)
    add.grid(row=1, column=2, columnspan=4)
    
    complete = tk.Button(root, text="Complete", command = complete_task)
    complete.grid(row=1, column=6, columnspan=4)

#creating the message box where the to-do list will be displayed
    message_box = scrolledtext.ScrolledText(root,wrap=tk.WORD, width= 60, height= 20)
    message_box.grid(row=2, column=4, columnspan=4)


    message_box.insert(tk.END, "Testing \n")
    #for i in range(len(list)):
        #message_box.insert(tk.END, f"{task_position}. {i}")






    root.mainloop()

if __name__ == "__main__":
    main()