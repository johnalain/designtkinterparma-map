#https://youtu.be/kPOm5OqHqWM?list=PLlvFEn0NKwXJGg6-Hs3yir4HCz9jw9UIs
#https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/
#pycharm guide https://www.jetbrains.com/guide/python/
from tkinter import *
myFrame =Tk()
myFrame.title("my app")
myFrame.geometry("500x500")

mybutton = Button(myFrame, text="click me",fg="blue", bg="yellow",font="helvetica 20 bold")
mybutton.pack()

myFrame.mainloop()