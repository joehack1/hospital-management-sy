import sqlite3
import tkinter as tk
from tkinter import ttk
tree = None

# Function to fetch and display patient data
def display_patients():
    
    global tree 
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
    tree = ttk.Treeview(display_window, columns=("ID", "Name", "Age", "Sex", "Contact"), show="headings")
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

# Function to edit patient data
def edit_patient():
    
    global tree  # Use the global tree variable
    if tree is None:
   
        return  # No patient selected

    # Create a new window for editing patient data
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Patient Data")

    # Get the patient ID of the selected item
    patient_id = tree.item(selected_item, 'values')[0]

    # Connect to the SQLite database for patients
    conn = sqlite3.connect('hmsdb.db')
    
    # Create a cursor object
    cursor = conn.cursor()

    # Execute an SQL query to retrieve the patient's data by ID
    cursor.execute("SELECT * FROM patient WHERE ID=?", (patient_id,))
    
    # Fetch the patient's data
    patient_data = cursor.fetchone()

    # Entry fields for editing patient data
    name_label = ttk.Label(edit_window, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(edit_window)
    name_entry.insert(0, patient_data[1])  # Fill the entry with the existing name
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    age_label = ttk.Label(edit_window, text="Age:")
    age_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    age_entry = ttk.Entry(edit_window)
    age_entry.insert(0, patient_data[2])  # Fill the entry with the existing age
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    sex_label = ttk.Label(edit_window, text="Sex:")
    sex_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    sex_entry = ttk.Entry(edit_window)
    sex_entry.insert(0, patient_data[3])  # Fill the entry with the existing sex
    sex_entry.grid(row=2, column=1, padx=5, pady=5)

    contact_label = ttk.Label(edit_window, text="Contact:")
    contact_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    contact_entry = ttk.Entry(edit_window)
    contact_entry.insert(0, patient_data[4])  # Fill the entry with the existing contact
    contact_entry.grid(row=3, column=1, padx=5, pady=5)

    # Function to save the edited data
    def save_edited_data():
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_sex = sex_entry.get()
        new_contact = contact_entry.get()

        # Update the patient data in the database
        cursor.execute("UPDATE patient SET name=?, age=?, sex=?, contact=? WHERE ID=?", (new_name, new_age, new_sex, new_contact, patient_id))
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

        # Close the edit window
        edit_window.destroy()

        # Refresh the patient data display
        display_patients()

    # Button to save the edited data
    save_button = ttk.Button(edit_window, text="Save", command=save_edited_data)
    save_button.grid(row=4, columnspan=2, padx=5, pady=10)

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
    tree = ttk.Treeview(search_window, columns=("ID", "Name", "Age", "Sex", "Contact"), show="headings")
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
    tree = ttk.Treeview(display_window, columns=("ID", "Username", "Name", "Specialty", "Contact"), show="headings")
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

# Create a frame for adding a new patient
add_frame = ttk.LabelFrame(root, text="Add New Patient")
add_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Entry fields for adding a new patient
name_label = ttk.Label(add_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(add_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

age_label = ttk.Label(add_frame, text="Age:")
age_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
age_entry = ttk.Entry(add_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

sex_label = ttk.Label(add_frame, text="Sex:")
sex_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
sex_entry = ttk.Entry(add_frame)
sex_entry.grid(row=2, column=1, padx=5, pady=5)

contact_label = ttk.Label(add_frame, text="Contact:")
contact_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
contact_entry = ttk.Entry(add_frame)
contact_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons for adding a new patient and searching
add_button = ttk.Button(add_frame, text="Add Patient", command=add_patient)
add_button.grid(row=4, columnspan=2, padx=5, pady=10)

# Create a frame for searching patients
search_frame = ttk.LabelFrame(root, text="Search Patients")
search_frame.pack(padx=10, pady=10, fill="both", expand="yes")

# Entry field and button for searching a patient by name
search_label = ttk.Label(search_frame, text="Search by Name:")
search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)
search_button = ttk.Button(search_frame, text="Search", command=search_patient)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Button to fetch and display all patient data
fetch_button = ttk.Button(root, text="Fetch Patient Data", command=display_patients)
fetch_button.pack(pady=10)

# Button to fetch and display doctors' data
fetch_doctors_button = ttk.Button(root, text="Fetch Doctors Data", command=display_doctors)
fetch_doctors_button.pack(pady=10)

# Button to edit patient data
edit_button = ttk.Button(root, text="Edit Patient Data", command=edit_patient)
edit_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
