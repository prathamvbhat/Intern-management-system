mport tkinter as tk
from tkinter import messagebox
import mysql.connector

# Initialize the Tkinter window
root = tk.Tk()
root.title("Find Intern")

# Create a function to connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root@localhost",
            password="Levin2003",
            database="FindIntern"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

# Function to add a new intern
def register_intern():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        age = int(entry_age.get())
        reg_no = int(entry_regno.get())
        dob = entry_dob.get()
        Address = entry_Address.get()
        Branch = entry_Branch.get()
        Gender = entry_Gender.get()
        try:
            cursor.execute("INSERT INTO Interns (first_name, last_name, email, phone, age, reg_no, DOB, Address, Branch, Gender) VALUES (%s, %s, %s, %s, %d, %d, , %s, %s, %s)",
                           (first_name, last_name, email, phone, age, reg_no, dob, Address, Branch, Gender))
            conn.commit()
            messagebox.showinfo("Success", "Intern added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

# Function to search for an intern
def search_intern():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        search_term = entry_search.get()
        cursor.execute("SELECT * FROM Interns WHERE first_name LIKE %s OR last_name LIKE %s", (f"%{search_term}%", f"%{search_term}%"))
        interns = cursor.fetchall()
        if interns:
            results_text.delete(1.0, tk.END)
            for intern in interns:
                results_text.insert(tk.END, f"ID: {intern[0]}\nFirst Name: {intern[1]}\nLast Name: {intern[2]}\nEmail: {intern[3]}\nPhone: {intern[4]}\n\n")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "No matching interns found.")
        cursor.close()
        conn.close()

# Create and configure the GUI elements
label_first_name = tk.Label(root, text="First Name:")
entry_first_name = tk.Entry(root)
label_last_name = tk.Label(root, text="Last Name:")
entry_last_name = tk.Entry(root)
label_regno = tk.Label(root, text="Register number:")
entry_regno = tk.Entry(root)
label_dob = tk.Label(root, text="Date of Birth:")
entry_dob = tk.Entry(root)
label_Address = tk.Label(root, text="Address:")
entry_Address = tk.Entry(root)
label_Branch = tk.Label(root, text="Branch:")
entry_Branch = tk.Entry(root)
label_Gender = tk.Label(root, text="Gender:")
entry_Gender = tk.Entry(root)
label_age = tk.Label(root, text="Age:")
entry_age = tk.Entry(root)
label_email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root)
label_phone = tk.Label(root, text="Phone:")
entry_phone = tk.Entry(root)

button_register = tk.Button(root, text="Register Intern", command=register_intern)
label_search = tk.Label(root, text="Search Interns:")
entry_search = tk.Entry(root)
button_search = tk.Button(root, text="Search", command=search_intern)
results_text = tk.Text(root, height=10, width=40)

# Place GUI elements on the window
label_first_name.pack()
entry_first_name.pack()
label_last_name.pack()
entry_last_name.pack()
label_email.pack()
entry_email.pack()
label_phone.pack()
entry_phone.pack()
label_regno.pack()
entry_regno.pack()
label_dob.pack()
entry_dob.pack()
label_Address.pack()
entry_Address.pack()
label_Branch.pack()
entry_Branch.pack()
label_Gender.pack()
entry_Gender.pack()
button_register.pack()
label_search.pack()
entry_search.pack()
button_search.pack()
results_text.pack()

# Start the Tkinter main loop
root.mainloop()
