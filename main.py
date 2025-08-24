def main():
    import tkinter as tk
    from tkinter import ttk


#make the program window
    root = tk.Tk()
    root.title("Test Title")
    root.minsize(250, 100)
    root.maxsize(500, 800)
    root.geometry("500x500")

    tk.Label(root, text = "To-Do List").pack()

    

    root.mainloop()

if __name__ == "__main__":
    main()