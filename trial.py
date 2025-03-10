import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch and display patient data
def display_patients():
    # Connect to the SQLite database for patients
    conn = sqlite3.connect('hmsdb.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute an SQL query to retrieve all patients' data
    cursor.execute("SELECT * FROM patient")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Create a new window for displaying patient data
    display_window = tk.Toplevel(root)
    display_window.title("Patient Data")

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(display_window, columns=("ID", "Name", "Age", "Sex", "Contact"), show="headings", style="Custom.Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Sex", text="Sex")
    tree.heading("Contact", text="Contact")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(padx=10, pady=10)
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()

# Function to add a new patient to the database
def add_patient():
    name = name_entry.get()
    age = age_entry.get()
    sex = sex_entry.get()
    contact = contact_entry.get()

    # Connect to the SQLite database for patients
    conn = sqlite3.connect('hmsdb.db')
    
    # Create a cursor object
    cursor = conn.cursor()

    # Insert a new patient into the database
    cursor.execute("INSERT INTO patient (name, age, sex, contact) VALUES (?, ?, ?, ?)",
                   (name, age, sex, contact))

    # Commit the transaction to save the new patient
    conn.commit()
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Clear the entry fields after adding the patient
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

# Function to search for a patient by name
def search_patient():
    search_name = search_entry.get()

    # Connect to the SQLite database for patients
    conn = sqlite3.connect('hmsdb.db')
    
    # Create a cursor object
    cursor = conn.cursor()

    # Execute an SQL query to search for a patient by name
    cursor.execute("SELECT * FROM patient WHERE name LIKE ?", ('%' + search_name + '%',))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Create a new window for displaying search results
    search_window = tk.Toplevel(root)
    search_window.title("Search Results")

    # Create a Treeview widget to display the search results
    tree = ttk.Treeview(search_window, columns=("ID", "Name", "Age", "Sex", "Contact"), show="headings", style="Custom.Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Sex", text="Sex")
    tree.heading("Contact", text="Contact")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(padx=10, pady=10)
    
    # Close the cursor and the database connection
    cursor.close()
    conn.close()


    

# Function to fetch and display doctors' data
def display_doctors():
    # Connect to the SQLite database for doctors
    conn = sqlite3.connect('doctorsdb.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute an SQL query to retrieve all doctors' data
    cursor.execute("SELECT * FROM doctors")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Create a new window for displaying doctor data
    display_window = tk.Toplevel(root)
    display_window.title("Doctor Data")

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(display_window, columns=("ID", "Username", "Name", "Specialty", "Contact"), show="headings", style="Custom.Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Username", text="Username")
    tree.heading("Name", text="Name")
    tree.heading("Specialty", text="Specialty")
    tree.heading("Contact", text="Contact")

    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(padx=10, pady=10)

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

# Create the main application window
root = tk.Tk()
root.title("Patient and Doctor Information")
root.configure(bg='#154360')  # Set background color to blue

# Create a custom style for the Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.Treeview.Heading", font=('Helvetica', 10, 'bold'), background='#154360', foreground='gold')
style.configure("Custom.Treeview", font=('Helvetica', 10), background='#1f618d', foreground='white', fieldbackground='#1f618d')

# Create a frame for adding a new patient
add_frame = ttk.LabelFrame(root, text="Add New Patient", style="Custom.TFrame")
add_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Entry fields for adding a new patient
name_label = ttk.Label(add_frame, text="Name:", style="Custom.TLabel")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(add_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = ttk.Label(add_frame, text="Age:", style="Custom.TLabel")
age_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
age_entry = ttk.Entry(add_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

sex_label = ttk.Label(add_frame, text="Sex:", style="Custom.TLabel")
sex_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
sex_entry = ttk.Entry(add_frame)
sex_entry.grid(row=2, column=1, padx=5, pady=5)

contact_label = ttk.Label(add_frame, text="Contact:", style="Custom.TLabel")
contact_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
contact_entry = ttk.Entry(add_frame)
contact_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for adding a new patient and searching
add_button = ttk.Button(add_frame, text="Add Patient", command=add_patient, style="Custom.TButton")
add_button.grid(row=4, columnspan=2, padx=5, pady=10)

# Create a frame for searching patients
search_frame = ttk.LabelFrame(root, text="Search Patients", style="Custom.TLabelframe")
search_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Entry field and button for searching a patient by name
search_label = ttk.Label(search_frame, text="Search by Name:", style="Custom.TLabel")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = ttk.Button(search_frame, text="Search", command=search_patient, style="Custom.TButton")
search_button.grid(row=0, column=2, padx=5, pady=5)

# Button to fetch and display all patient data
fetch_button = ttk.Button(root, text="Fetch Patient Data", command=display_patients, style="Custom.TButton")
fetch_button.pack(pady=10)

# Button to fetch and display doctors' data
fetch_doctors_button = ttk.Button(root, text="Fetch Doctors Data", command=display_doctors, style="Custom.TButton")
fetch_doctors_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
