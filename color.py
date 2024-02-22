# import tkinter as Tk
import tkinter as tk
from tkmacosx import Button

     
root=tk.Tk()
root.geometry('220x120')
root.title('change colopadx=10,pady=10r')
root.configure(background='red')


    

b1 = tk.Button(root,text='click me')
b2 = tk.Button(root,text='click me')

b1.grid(row = 1, column =1,)
b2.grid(row = 1, column =2,padx=10,pady=10)
root.mainloop()