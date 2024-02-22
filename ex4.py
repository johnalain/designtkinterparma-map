#https://youtu.be/CplixCzrN1Q?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v
from tkinter import *
pro = Tk()
pro.geometry('800x500')
fr1 = Frame(width='390', height='499',bg='red')
fr1.place(x=1, y=1)

fr2 = Frame(width='390', height='499',bg='blue')
fr2.place(x=393, y=1)

bt1 = Button (fr1,text='button1',fg='black',bg='white',width=30)
bt1.place(x=10,y=10)

bt2 = Button (fr2,text='button1',fg='black',bg='red',cursor='heart',width=20)
bt2.place(x=10,y=10)

lb1 =Label(fr1,text='st.Rita Pharmacy ',
           fg='black',bg='#C7C550',font=20)
lb1.place(x=10,y=40)

lb2 =Label(fr2,text='st.Rita Pharmacy',fg='black',bg='#C7C550',font=10)
lb2.place(x=10,y=40)

lb3 =Label(fr2,text='beauty accessories',fg='black',bg='#C7C550',font=20)
lb3.place(x=10,y=70)

pro.mainloop()
#https://youtu.be/7Dd_kp21VvY?list=PLSiLeKadTQ7nLJxpQo1-944miQKlheu-v