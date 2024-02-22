#https://youtu.be/DFHFSpo5dvI?t=691
from tkinter import *
from tkintermapview import TkinterMapView

root = Tk()
root.geometry('880x450')
root.title('St. rita pharmacies in duty')
root.iconbitmap('/Users/michelkadi/Desktop/supermarImage/images.png')
root.configure(background='#34a853')
def cu():
    country = En.get()
    #"http://mto.google.com/vt/lyrs=m&h1=en&x={x}&y={y}&z={z}&s=ga",max_zoom=22
    map.set_tile_server("http://mto.google.com/vt/lyrs=m&h1=en&x={x}&y={y}&z={z}&s=ga",max_zoom=22)
    map.set_address(country,marker=True)
title1 = Label(root,text='St Rita pharmacy',fg='black',bg=	'#fbbc05',font=('Tajawal',16,'italic'))

title1.pack(fill=X)

logo = PhotoImage(file='/Users/michelkadi/Desktop/supermarImage/download (1).png')
lab_logo = Label(root,image=logo,bd=0,bg='white')
lab_logo.place(x=2,y=27)

l = Label(root,text='country',bg='white',fg='black')
l.place(x=10,y=260)
#https://youtu.be/DFHFSpo5dvI?t=1040
En = Entry(root,font=('Tajawala',14),width=10,bd=2,relief=GROOVE)
En.place(x=80,y=260)

b1 = Button(root,text='get country',
            fg='black',bg='black',bd=1,
            relief=SOLID,width=10,cursor='hand2',command=cu)
b1.place(x=240,y=260)
#pharmacy buttons
b2 = Button(root,text='central pharmacy',
           fg='black',bg='black',bd=2,
           relief=GROOVE,width=13,cursor='hand',
           font=('Tajawal,12 '))
b2.place(x = 10,y = 300)

b3 = Button(root,text='mazraa pharmacy',
            fg='black',bg='black',bd=2,
            relief=SOLID,width=13,cursor='hand',
            padx=15,font=('Tajawal,12 '))
b3.place(x = 160,y = 300)

b4 = Button(root,text='salhieh pharmacy',
            fg='black',bg='black',bd=1,
            relief=SOLID,width=13,cursor='hand',
            font=('Tajawal,12 '))
b4.place(x = 340,y = 300)

b5 = Button(root,text='jounieh pharmacy',
            fg='black',bg='black',bd=3,
            relief=SOLID,width=13,cursor='hand',
            font=('Tajawal,12 '))
b5.place(x = 10,y = 340)

b6 = Button(root,text='baabdat pharmacy',
            fg='black',bg='black',bd=3,
            relief=SOLID,width=13,cursor='hand',
            font=('Tajawal,12 '))
b6.place(x = 150,y = 340)

# b7 = Button(root,text='jbeil pharmacy',
#             fg='black',bg='black',bd=3,
#             relief=SOLID,width=13,cursor='hand',
#             font=('Tajawal,12 '))
# b7.place(x = 180,y = 340)

b8 = Button(root,text='aanya pharmacy',
            fg='black',bg='black',bd=3,
            relief=SOLID,width=13,cursor='hand',
            font=('Tajawal,12 '))
b8.place(x = 300,y = 340)


map = TkinterMapView(root,width=800,height=200,corner_radius=0)
map.place(x=390,y=45)


root.mainloop()