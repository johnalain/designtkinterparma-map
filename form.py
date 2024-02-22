#https://youtu.be/NBtlWVXNNtE?t=263
from tkinter import *
from colour import Color
window=Tk()
window.geometry('400x300')
window.title('registration form')
def print():
    print('demo registration form')

def exit():
    exit()
    
label1 = Label(window, text = 'Registration form',relief='solid',bg='#8A2BE2',font=('arial',16,'bold'))
label1.place(x=90,y=53)
b = Button(window, text = 'hello to eery one',fg='red',bg='#8A2BE2',font=('arial',16,'bold'))
b.place(x=85,y=75)



window.mainloop()
