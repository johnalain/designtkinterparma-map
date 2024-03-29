# https://www.youtube.com/watch?v=vusUfPBsggw&list=PLlvFEn0NKwXKKGUESVoKdeC6umLFKcAlk&index=1&t=132s
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("data entry form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame,text="user information")
user_info_frame.grid(row=0,column=0,padx=20 ,pady=10)

first_name_label = tkinter.Label(user_info_frame,text="First name")
first_name_label.grid(row=0,column=0)

last_name_label = tkinter.Label(user_info_frame,text="Last name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title")
title_combobox =ttk.Combobox(user_info_frame,values=["","Mr","Ms","Dr"])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=110)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label=tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=["Africa","Europe","Asia","north America","south America"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)
# time:24:20
# for Widget in user_info_frame.widget_children():
#     Widget.grid_configure(padx=10,pady=5)
for Widget in user_info_frame.winfo_children():
    Widget.grid_configure(padx=10,pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_label = tkinter.Label(courses_frame,text="Registration status")
registered_check = tkinter.Checkbutton(courses_frame,text="currently registered")
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label = tkinter.Label(courses_frame,text="#completed courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to ="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label=tkinter.Label(courses_frame,text='#semesters') 
numsemesters_spinbox=tkinter.Spinbox(courses_frame,from_=0,to='infinity')
numsemesters_label.grid(row=0,column=4)
numsemesters_spinbox.grid(row=1,column=4)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    
    terms_frame=tkinter.LabelFrame(frame,text='terms & conditions')
    terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)
    terms_check=tkinter.Checkbutton(terms_frame,text="i accept terms and conditions")
    terms_check.grid(row=0,column=0)
    
    button = tkinter.Button(frame, text="Enter data")
    button.grid(row=3,column=0,sticky='news',padx=20,pady=10)
    # https://youtu.be/vusUfPBsggw?list=PLlvFEn0NKwXKKGUESVoKdeC6umLFKcAlk&t=2249
                                           


window.mainloop()
#right run python file
