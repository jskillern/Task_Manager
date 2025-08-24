import tkinter as tk
import os

FILE_NAME = "list_history.txt"

def ensure_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("")

def refresh_list(message_box):
    ensure_file()
    with open(FILE_NAME, "r") as file:
        content = file.read
    
    message_box.config(state=tk.NORMAL)
    message_box.delete("1.0", tk.END)
    message_box.insert(tk.END, content)
    message_box.config(state=tk.DISABLED)

def create_task(parent, message_box):
    popup = tk.Toplevel(parent)
    popup.minsize(400, 100)
    popup.geometry("400x100")
    popup.title("Add Task")

    tk.Label(popup, text="Enter new task").grid(row=0, column=0,padx=10, pady=5)
     
    user_input = tk.Entry(popup, width=30)
    user_input.grid(row=1, column=0, padx=10, pady=5)
    


    def add_task():
        task = user_input.get().strip()
        if task:
            with open(FILE_NAME, "a") as file:
                file.write(f"\n{task}")
            refresh_list(message_box)
        popup.destroy()

    tk.Button(popup, text="Add", command = add_task).grid(row=1, column=1, padx=10, pady=5)
    


def complete_task(message_box):
    ensure_file()
    with open(FILE_NAME, "r") as file:
        tasks = [line.strip() for line in file if line.strip()]
    if tasks:
        tasks.pop(0)  #edit this to be correct
        with open(FILE_NAME, "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
        refresh_list(message_box)