import customtkinter
from customtkinter import *
from PIL import Image
from tkinter import messagebox

customtkinter.set_appearance_mode("light")


def login():
    if userName.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','All fields are required.')
    elif userName.get()=='admin' and passwordEntry.get()=='admin':
        messagebox.showinfo('Success', 'Successfully logged in!')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Invalid credentials')

root = CTk()
root.geometry('860x480')
root.configure(bg="white")
root.resizable(0,0)
root.title('Login Page')
image = CTkImage(Image.open('img/login.png'),size=(860,480))
imageLabel=CTkLabel(root,image=image, text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='AdminiSphere',bg_color= 'white', corner_radius=5, text_color='#1A0F91',font=('Calibri',35,'bold'))
headingLabel.place(x=97,y=80)


userName = CTkEntry(root, placeholder_text='Enter username', placeholder_text_color='grey', border_color='#6C6C70', border_width=2, fg_color='white', bg_color='white', text_color= 'black', corner_radius=2, width=270, height=30)
userName.place(x=75,y=135)

passwordEntry = CTkEntry(root, placeholder_text='Enter password', show = '*', placeholder_text_color='grey', border_color='#6C6C70', border_width=2, fg_color='white', bg_color='white', text_color= 'black',corner_radius=2, width=270, height=30)
passwordEntry.place(x=75,y=175)

loginButton = CTkButton(root,text='Login', cursor='hand2', command=login, bg_color='white', fg_color='#484BF2', hover_color= '#180E8B', height=40, width=130)
loginButton.place(x=142,y=225)

root.mainloop()
