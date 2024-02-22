#https://youtu.be/TuLxsvK4svQ?list=PLlvFEn0NKwXKMpQhQCpOa1AXIQ20s6_ex&t=1169
from tkinter import *
#outside thewindow create a function that works with button command
count=0
def click():
    global count
    count=count+1
    print(count)
# def click():
#     print("you clicked the button")

window=Tk()
photo = PhotoImage(file='//Users//michelkadi//Desktop//supermarImage//download.png')

button =Button(window,
               text='click me',
               command=click,
               activeforeground='red',
               activebackground='black',
                state=ACTIVE,# by default is Active
               image=photo,
               compound='bottom'#for compound u can use top left right as well
               
            )
button.pack()

window.mainloop()