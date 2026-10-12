from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import ast
import os

SCREEN = Tk()
SCREEN.title("Address Book")
SCREEN.geometry("720x520")
SCREEN.config(background="#d9d9d9")
addressbook = {}

def clearall():
    nameentry.delete(0,END)
    addressentry.delete(0,END)
    mobileentry.delete(0,END)
    emailentry.delete(0,END)
    birthdayentry.delete(0,END)

def update():
    written = nameentry.get()
    if written == "":
        messagebox.showerror("Error","Name Cannot Be Empty!")
    else:
        if written not in addressbook.keys():
            book_list.insert(END,written)
        addressbook[written]=(addressentry.get(),mobileentry.get(),emailentry.get(),birthdayentry.get())
    clearall()

def display(event):
    newwindow = Toplevel(SCREEN)
    index = book_list.curselection()
    contact = ""
    if index:
        key = book_list.get(index)
        contact = "name: " + key + "\n"
        details = addressbook[key]
        contact += "address: " + details[0]+"\n"
        contact += "mobile: " + details[1]+"\n"
        contact += "email: " + details[2]+"\n"
        contact += "birthday: " + details[3]+"\n"
    le_output = Label(newwindow)
    le_output.place(x=10,y=10)
    le_output.configure(text=contact)

def save():
    storage = asksaveasfile(defaultextension=".txt")
    if storage:
        print(addressbook,file=storage)
        reset()
    else:
        messagebox.showerror("Error","Address book Not Saved!")

def edit():
    clearall()
    index = book_list.curselection()
    if index:
        nameentry.insert(0,book_list.get(index))
        details = addressbook[nameentry.get()]
        addressentry.insert(0,details[0])
        mobileentry.insert(0,details[1])
        emailentry.insert(0,details[2])
        birthdayentry.insert(0,details[3])
    else:
        messagebox.showerror("ERROR","Select a name!")

def delete():
    index = book_list.curselection()
    if index:
        del addressbook[book_list.get(index)]
        book_list.delete(index)
        clearall()
    else:
        messagebox.showerror("ERROR","Select a name!")

def reset():
    clearall()
    book_list.delete(0,END)
    addressbook.clear()
    myaddressbooklab.configure(text="My Address Book")

def open():
    global addressbook
    addressbook_file = askopenfile(title="Open File")
    if not addressbook_file:
        return
    try:
        with addressbook_file:
            loaded_addressbook = ast.literal_eval(addressbook_file.read())
        if not isinstance(loaded_addressbook, dict):
            raise ValueError("The selected file is not an address book.")
    except (OSError, SyntaxError, ValueError) as error:
        messagebox.showerror("ERROR", f"Could not open address book: {error}")
        return

    reset()
    addressbook = loaded_addressbook
    for name in addressbook:
        book_list.insert(END, name)
    myaddressbooklab.configure(text=os.path.basename(addressbook_file.name))

myaddressbooklab = Label(SCREEN, text="My Address Book", font=("Arial", 18))
myaddressbooklab.place(x=20, y=12)

openbutton = Button(SCREEN, text="Open", width=12,command=open)
openbutton.place(x=470, y=12)

book_list = Listbox(SCREEN, width=30, height=18)
book_list.place(x=20, y=80)
book_list.bind("<<ListboxSelect>>",display)

Label(SCREEN, text="Name:").place(x=390, y=105)
nameentry = Entry(SCREEN, width=24)
nameentry.place(x=490, y=105)

Label(SCREEN, text="Address:").place(x=390, y=165)
addressentry = Entry(SCREEN, width=24)
addressentry.place(x=490, y=165)

Label(SCREEN, text="Mobile:").place(x=390, y=225)
mobileentry = Entry(SCREEN, width=24)
mobileentry.place(x=490, y=225)

Label(SCREEN, text="Email:").place(x=390, y=285)
emailentry = Entry(SCREEN, width=24)
emailentry.place(x=490, y=285)

Label(SCREEN, text="Birthday:").place(x=390, y=345)
birthdayentry = Entry(SCREEN, width=24)
birthdayentry.place(x=490, y=345)

editbutton = Button(SCREEN, text="Edit", width=10,command=edit)
editbutton.place(x=20, y=420)

deletebutton = Button(SCREEN, text="Delete", width=10,command=delete)
deletebutton.place(x=140, y=420)

updatebutton = Button(SCREEN, text="Update/Add", width=12, command=update)
updatebutton.place(x=490, y=420)

savebutton = Button(SCREEN, text="Save", width=28,command=save)
savebutton.place(x=185, y=470)

mainloop()