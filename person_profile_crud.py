import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


conn = sqlite3.connect("profiles.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT NOT NULL,
        "email" TEXT NOT NULL,
        "phone" TEXT NOT NULL,
        "city" TEXT NOT NULL,
        "age" INTEGER NOT NULL,
        "occupation" TEXT NOT NULL)
""")

conn.commit()

#CREATE

def add_profile():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if name == "" or email == "" or phone == "" or city =="" or age == "" or occupation == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number."
        )
        return

    cursor.execute(
        "INSERT INTO profiles (name, email, phone, city,  age, occupation) VALUES (?, ?, ?, ?, ?, ?)",
        (name, email, phone, city, age, occupation)
    )

    conn.commit()

    messagebox.showinfo(
        "Success",
        "profile added successfully."
    )

    clear_fields()
    display_profiles()

# READ
def display_profile():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM profiles")

    profiles = cursor.fetchall()

    for profile in profiles:
        tree.insert("", tk.END, values=profile)

# UPDATE
def update_profile():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to update."
        )
        return

    profile_id = tree.item(selected[0000])["values"][0]

    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()
    age = age_entry.get()
    occupation = occupation_entry.get()

    if name == "" or email == "" or phone == "" or city =="" or age == "" or occupation == "":
        messagebox.showwarning(
            "Warning",
            "Please fill in all fields."
        )
        return

    try:
        age = int(age)
        name=str(name)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number.Name should be in String Form"
        )
        return

    cursor.execute("""
        UPDATE profiles
        SET name = ?, email = ?, phone = ?, city = ?, age = ?, occupation = ?
        WHERE id = ?
    """, (name, email, phone, age, occupation, profile_id))

    conn.commit()

    messagebox.showinfo(
        "Success",
        "Profile updated successfully."
    )

    clear_fields()
    display_profiles()

# DELETE
def delete_profile():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a profile to delete."
        )
        return

    profile_id = tree.item(selected[0])["values"][0]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this profile?"
    )

    if confirm:
        cursor.execute(
            "DELETE FROM profiles WHERE id = ?",
            (profile_id,)
        )
        conn.commit()
        messagebox.showinfo(
            "Success",
            "profile deleted successfully."
        )

        clear_fields()
        display_profiles()


# CLEAR INPUTS
def clear_fields():

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    occupation_entry.delete(0, tk.END)

# SELECT PROFILE
def select_profile(event):
    selected = tree.selection()

    if selected:
        profile = tree.item(selected[0])["values"]

        clear_fields()
        name_entry.insert(0, profile[1])
        email_entry.insert(0, profile[2])
        phone_entry.insert(0, profile[3])
        city_entry.insert(0, profile[4])
        age_entry.insert(0, profile[5])
        occupation_entry.insert(0, profile[6])
    

root = tk.Tk()
root.title("Person Profile System")
root.geometry("700x500")

title_label = tk.Label(
    root,
    text="Person Profile System",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

#NAME
tk.Label(
    input_frame,
    text="Name :"
).grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(input_frame, width=50)
name_entry.grid(row=0, column=1, padx=5, pady=5)

#EMAIL
tk.Label(
    input_frame,
    text="Email :"
).grid(row=1, column=0, padx=5, pady=5)

email_entry = tk.Entry(input_frame, width=50)
email_entry.grid(row=1, column=1, padx=5, pady=5)

#PHONE
tk.Label(
    input_frame,
    text="Phone No. :"
).grid(row=2, column=0, padx=5, pady=5)

phone_entry = tk.Entry(input_frame, width=50)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

#CITY
tk.Label(
    input_frame,
    text="City :"
).grid(row=3, column=0, padx=5, pady=5)

city_entry = tk.Entry(input_frame, width=50)
city_entry.grid(row=3, column=1, padx=5, pady=5)

#AGE
tk.Label(
    input_frame,
    text="Age :"
).grid(row=4, column=0, padx=5, pady=5)

age_entry = tk.Entry(input_frame, width=50)
age_entry.grid(row=4, column=1, padx=5, pady=5)

#OCCUPATION
tk.Label(
    input_frame,
    text="Occupation :"
).grid(row=5, column=0, padx=5, pady=5)

occupation_entry = tk.Entry(input_frame, width=50)
occupation_entry.grid(row=5, column=1, padx=5, pady=5)

#BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text = "Add",
    width = 10,
    command=add_profile
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text = "Update",
    width = 10,
    command=update_profile
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text = "Delete",
    width = 10,
    command=delete_profile
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text = "Clear",
    width = 10,
    command=clear_fields
).grid(row=0, column=3, padx=5)

#TABLE
tree = ttk.Treeview(
    root,
    columns=("ID", "Name", "Email", "Phone", "City", "Age", "Occupation"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Phone", text="Phone")
tree.heading("City", text="City")
tree.heading("Age", text="Age")
tree.heading("Occupation", text="Occupation")

tree.column("ID", width=50)
tree.column("Name", width=200)
tree.column("Email", width=200)
tree.column("Phone", width=100)
tree.column("City", width=200)
tree.column("Age", width=80)
tree.column("Occupation", width=200)


tree.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

