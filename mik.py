import tkinter
from tkinter import ttk

from sqlalchemy import values

window=tkinter.Tk()
window.title("ritajosephine")
frame=tkinter.Frame(window)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text="user information")
user_info_frame.grid(row=0,column=0,padx=30,pady=40)
first_name_label=tkinter.Label(user_info_frame,text="first name")
first_name_label.grid(row=0,column=0)

last_name_label=tkinter.Label(user_info_frame,text="last name")
last_name_label.grid(row=0,column=1)

last_name_label =tkinter.Label(user_info_frame,text="last name")
last_name_label.grid(row=0,column=1)

first_name_entry =tkinter.Entry(user_info_frame)
last_name_entry =tkinter.Entry(user_info_frame)

first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label=tkinter.Label(user_info_frame,text="title")
title_combobox=ttk.Combobox(user_info_frame,values=["","Mr.","Ms","Dr."])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)


window.mainloop()