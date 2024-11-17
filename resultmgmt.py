import sqlite3
from tkinter import *

# Database setup
conn = sqlite3.connect("student_results.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
""")
conn.commit()

# Functions
def add_record():
    name = entry_name.get()
    subject = entry_subject.get()
    marks = entry_marks.get()
    cursor.execute("INSERT INTO results (name, subject, marks) VALUES (?, ?, ?)", (name, subject, marks))
    conn.commit()
    label_message.config(text="Record added successfully!")

def view_records():
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()
    text_records.delete("1.0", END)
    for row in rows:
        text_records.insert(END, f"ID: {row[0]}, Name: {row[1]}, Subject: {row[2]}, Marks: {row[3]}\n")

# UI Setup
root = Tk()
root.title("Student Result Management")

Label(root, text="Name").grid(row=0, column=0)
entry_name = Entry(root)
entry_name.grid(row=0, column=1)

Label(root, text="Subject").grid(row=1, column=0)
entry_subject = Entry(root)
entry_subject.grid(row=1, column=1)

Label(root, text="Marks").grid(row=2, column=0)
entry_marks = Entry(root)
entry_marks.grid(row=2, column=1)

Button(root, text="Add Record", command=add_record).grid(row=3, column=0, pady=10)
Button(root, text="View Records", command=view_records).grid(row=3, column=1, pady=10)

text_records = Text(root, width=50, height=10)
text_records.grid(row=4, column=0, columnspan=2)

label_message = Label(root, text="", fg="green")
label_message.grid(row=5, column=0, columnspan=2)

root.mainloop()
