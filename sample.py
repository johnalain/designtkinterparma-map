#https://youtu.be/wQf9y2Bg8bo
import tkinter as tk
def exit():
    print('rita')
    
r = tk.Tk()
r.title('im learning')
b=tk.Button(r,text='Save',fg='red',command=exit)
b.place(x=20,y=20)
label=tk.Label(r,text='michel',fg='blue',bg='cyan')
label.place(x=30,y=45)
r.mainloop()