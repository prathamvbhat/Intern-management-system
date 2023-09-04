from tkinter import *
from PIL import ImageTk, Image
#import mysql.connector 

#Creating main window for GUI
root = Tk()

#Sets the dimension of the window
root.title("INTERNSHIP MANAGEMENT SYSTEM")
root.geometry('400x350')

#Connect Databases
#conn = mysql.connector.connect(user = '', localhost = ' ', database = 'MyIntern.db')

#cur = conn.cursor()
#conn.commit()

#Changes the title of the window
# label = Label(root, text="INTERNSHIP MANAGEMENT SYSTEM", font=('Times new roman',26)).place(relx = 1, rely =1, anchor = N)
# label.grid(roe)

#saves all values from the text fields and uploads to database
def submit_find():
    #Clear all text boxes
    return

#saves all values from register and updates to database
def submit_register():
    #clear all text boxes
    return

def register():
    top = Toplevel()
    top.geometry('700x400')

    #create labels
    name_label = Label(top, text="Name:").grid(row=1, column=0)
    Id_label = Label(top, text="Register Number:").grid(row=2, column=0)
    branch_label = Label(top, text="Branch:").grid(row=3, column=0)
    age_label = Label(top, text="Age:").grid(row=4, column=0)
    gender_label = Label(top, text="Gender:").grid(row=5, column=0)
    Dob_label = Label(top, text="DOB:").grid(row=6, column=0)
    email_label = Label(top, text="E-mail:").grid(row=7, column=0)
    Address_label = Label(top, text="Address:").grid(row=8, column=0)
    Phone_label = Label(top, text="Phone number:").grid(row=9, column=0)
    position_label = Label(top, text="Position").grid(row=10, column=0)
    workExp_label = Label(top, text="Work Experience:").grid(row=11, column=0)

    #create text boxes
    name = Entry(top, width=50).grid(row=1, column=2)
    Id = Entry(top, width=50).grid(row=2, column=2)
    branch = Entry(top, width=50).grid(row=3, column=2)
    age = Entry(top, width=50).grid(row=4, column=2)
    gender = Entry(top, width=50).grid(row=5, column=2)
    Dob = Entry(top, width=50).grid(row=6, column=2)
    email = Entry(top, width=50).grid(row=7, column=2)
    Address = Entry(top, width=50).grid(row=8, column=2)
    Phone = Entry(top, width=50).grid(row=9, column=2)
    position = Entry(top, width=50).grid(row=10, column=2)
    workExp = Entry(top, width=50).grid(row=11, column=2)

    
    close = Button(top, text="Close", command=top.destroy).grid(row=14, column=1, columnspan=3, pady=10)
    sub = Button(top, text='submit', command=submit_register).grid(row=13, column=2, columnspan=3, pady=10)

def find():
    #same stuff as the previous register function with different text fields
    top1 = Toplevel()
    top1.geometry('700x400')

    #create labels
    branch_label = Label(top1, text="Branch:").grid(row=1, column=0)
    age_label = Label(top1, text="Age:").grid(row=2, column=0)
    Address_label = Label(top1, text="Address:").grid(row=3, column=0)
    position_label = Label(top1, text="Position").grid(row=4, column=0)
    workExp_label = Label(top1, text="Work Experience:").grid(row=5, column=0)

    #create text boxes
    branch = Entry(top1, width=50).grid(row=1, column=2)
    age = Entry(top1, width=50).grid(row=2, column=2)
    Address = Entry(top1, width=50).grid(row=3, column=2)
    position = Entry(top1, width=50).grid(row=4, column=2)
    workExp = Entry(top1, width=50).grid(row=5, column=2)

    
    close = Button(top1, text="Close", command=top1.destroy).grid(row=7, column=1, columnspan=3, pady=10)
    sub = Button(top1, text='submit', command=submit_find).grid(row=7, column=2, columnspan=3, pady=10)


#Creating buttons and Displays the buttons in the window
Register = Button(root, text = "Register", fg = "Black", command= register)
Find = Button(root, text = "Find", fg = "Black", command= find)
Update = Button(root, text="Update record", fg="black" )
delete = Button(root, text="Delete record", fg="Black")
leave = Button(root, text="Exit", fg = "Black", command=root.quit)

Register.pack(pady=20)
Find.pack(pady=10)
Update.pack(pady=10)
delete.pack(pady=10)
leave.pack(pady=20)

#conn.close()

#Runs it infinetly till closed by the user
root.mainloop()