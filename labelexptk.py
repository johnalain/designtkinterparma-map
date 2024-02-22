# https://youtu.be/TuLxsvK4svQ?list=PLlvFEn0NKwXKMpQhQCpOa1AXIQ20s6_ex
from tkinter import *
window = Tk()
photo=PhotoImage(file='//Users//michelkadi//Desktop//supermarImage//download.png')
label = Label(window,text='hello world bro code teaching tkinter',
font=('Arial',40,'bold'),fg='black',bg='white',
relief=RAISED,bd=10,padx=20,pady=20,image=photo,compound='bottom'
)
#we can use top for compound as well
#if we add more text the enlarge to contain the text
# label.place(x=0,y=0)
label.pack()
window.geometry('600x600')
window.title('brocode first GUI program')
# icon = PhotoImage(file='download.png')
# window.iconphoto(True,icon)
# window.config(background='#fff')
# label = Label(window,text = 'hello world',font=('Arial',40,'bold'),
# fg='black',bg='lightgreen',relief=RAISED,bd=10,
# padx=20,pady=20,
# image=photo,compound='bottom')


window.mainloop()
