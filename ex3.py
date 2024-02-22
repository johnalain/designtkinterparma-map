#https://youtu.be/2DJvnHieNp0?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v
from tkinter import *
pro = Tk()
pro.geometry('800x500')
fr1 = Frame(width='390', height='499',bg='red')
fr1.place(x=1, y=1)

fr2 = Frame(width='390', height='499',bg='blue')
fr2.place(x=393, y=1)

bt1 = Button (fr1,text='button1',fg='black',bg='white')
bt1.place(x=10,y=10)

bt2 = Button (fr2,text='button1',fg='black',bg='red',cursor='heart')
bt2.place(x=10,y=10)

pro.mainloop()
