#https://youtu.be/Z_0ISFfT_eM?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('comedy.com - learn to code')
root.iconbitmap('download.png')
root.geometry('400x400')
# my_text =Text(root,width=40,height=10,font=('Helvetica',16))
# my_text.pack(pady=20)

def open_text():
    # text_file = ('michel')
    text_file = open('TKINTER/message.text','r')
    stuff = text_file.read()
    text_file.insert(END, stuff)
    text_file.close()
    
    my_text = Text(root,width=40,height=10, font=("Helvetica",16))
    my_text.pack()
    open_button = Button (root,text="open text file",command=open_text)
    open_button.pack()
    #https://youtu.be/Z_0ISFfT_eM?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&t=461

root.mainloop()