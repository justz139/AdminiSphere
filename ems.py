import customtkinter
from customtkinter import *
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import db


#Functions

def delete_all():
   result=messagebox.askyesno('Warning', 'Are you sure you want to delete all employee records?')
   if result:
       db.delete_records()
       treeview_data()
   else:
       pass

def show_all():
    treeview_data()
    searchBox.set('Search by')

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter desired value to be searched')
    elif searchBox.get()=='Search by':
        messagebox.showerror('Error','Please select an option')
    else:
        searched_data=db.search(searchBox.get(), searchEntry.get())
        searchEntry.delete(0, END)
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('', END, values=employee)

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        db.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee deleted successfully!')

def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        db.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Records updated successfully!')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)

def treeview_data():
    employees=db.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)

def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif db.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', 'Invalid ID format. Use "EMP" followed by a number (e.g, "EMP1")')
    else:
        db.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Employee Registered!')

#GUI
customtkinter.set_appearance_mode("light")

window=CTk()
window.geometry('930x580+100+100')
window.title('AdminiSphere')
window.resizable(0,0)
window.configure(fg_color='#FFE2DC')
logo=CTkImage(Image.open('img/ems.jpg'),size=(930,158))
logoLabel=CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#FFE2DC')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='ID',text_color='#000000', font=('Roboto', 20, 'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('Calibri',15,'bold'), width= 180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',text_color='#000000', font=('Roboto', 20, 'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('Calibri',15,'bold'), width= 180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',text_color='#000000', font=('Roboto', 20, 'bold'))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('Calibri',15,'bold'), width= 180)
phoneEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',text_color='#000000', font=('Roboto', 20, 'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','DevOps Engineer','Data Scientist','Business Analyst','IT Consultant','UI/UX Designer']

roleBox=CTkComboBox(leftFrame,values=role_options,width= 180,font=('Calibri',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',text_color='#000000', font=('Roboto', 20, 'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options=['Male','Female']

genderBox=CTkComboBox(leftFrame,values=gender_options,width= 180,font=('Calibri',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salary',text_color='#000000', font=('Roboto', 20, 'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFrame,font=('Calibri',15,'bold'), width= 180)
salaryEntry.grid(row=5,column=1)

rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['ID','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,font=('Calibri',15,'bold'),state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search by')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,font=('Garamond',15,'bold'),fg_color='#44569E',hover_color= '#252557',command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show all',width=100,font=('Garamond',15,'bold'),fg_color='#44569E',hover_color= '#252557',command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',anchor=CENTER,width=80)
tree.column('Name',anchor=CENTER,width=150)
tree.column('Phone',anchor=CENTER,width=140)
tree.column('Role',anchor=CENTER,width=180)
tree.column('Gender',anchor=CENTER,width=100)
tree.column('Salary',anchor=CENTER,width=100)

style=ttk.Style()

style.configure('Treeview.Heading',font=('Calibri',16,'bold'))
style.configure('Treeview',font=('arial',13,'bold'), rowheight=25, background='#000000',foreground='white')

scrollBar=ttk.Scrollbar(rightFrame, orient=VERTICAL, command=tree.yview())
scrollBar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollBar.set)

buttonFrame=CTkFrame(window, fg_color='#FFE2DC')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text='New Employee',font=('Garamond',15,'bold'), width=160,corner_radius=15,fg_color='#44569E',hover_color= '#252557',command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('Garamond',15,'bold'), width=160,corner_radius=15,fg_color='#44569E',hover_color= '#252557', command=add_employee)
addButton.grid(row=0,column=1,pady=5, padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('Garamond',15,'bold'), width=160,corner_radius=15,fg_color='#44569E',hover_color= '#252557',command=update_employee)
updateButton.grid(row=0,column=2,pady=5, padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('Garamond',15,'bold'), width=160,corner_radius=15,fg_color='#44569E',hover_color= '#252557',command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5, padx=5)

delallButton=CTkButton(buttonFrame,text='Delete All',font=('Garamond',15,'bold'), width=160,corner_radius=15,fg_color='#44569E',hover_color= '#252557', command=delete_all)
delallButton.grid(row=0,column=4,pady=5, padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()
