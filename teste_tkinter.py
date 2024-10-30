import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Gerador de Proejto")
window.config(padx=50, pady=100)


label_entry = Label(text="Path Projeto")
label_entry.grid(row=0,column=0)

# Entrada
project_entry = Entry()
project_entry.grid(row=0,column=1,columnspan=2)



window.mainloop()

  
