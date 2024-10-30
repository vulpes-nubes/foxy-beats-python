import requests
import openpyxl
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox

# Function to get book details from Open Library
def get_book_details(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    data = response.json()
    
    if f'ISBN:{isbn}' in data:
        book_data = data[f'ISBN:{isbn}']
        title = book_data.get('title', 'N/A')
        authors = ', '.join(author['name'] for author in book_data.get('authors', []))
        year = book_data.get('publish_date', 'N/A')
        dewey = book_data.get('dewey_decimal_class', ['N/A'])[0]  # Only taking the first entry
        
        return title, authors, year, dewey
    else:
        return None

# Function to append or create Excel file
def update_excel(isbn, title, authors, year, dewey):
    file_name = 'books.xlsx'
    
    try:
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active
    except FileNotFoundError:
        wb = Workbook()
        sheet = wb.active
        sheet.append(['ISBN', 'Book Title', 'Author(s)', 'Year', 'Dewey Decimal'])

    sheet.append([isbn, title, authors, year, dewey])
    wb.save(file_name)

# Function to handle ISBN input
def on_submit():
    isbn = isbn_entry.get()
    if isbn:
        book_details = get_book_details(isbn)
        if book_details:
            title, authors, year, dewey = book_details
            update_excel(isbn, title, authors, year, dewey)
            messagebox.showinfo("Success", f"Added:\nISBN: {isbn}\nTitle: {title}\nAuthors: {authors}\nYear: {year}\nDewey: {dewey}")
        else:
            messagebox.showwarning("Error", "No book found for this ISBN.")
    else:
        messagebox.showwarning("Error", "Please enter an ISBN.")

# Create GUI
root = tk.Tk()
root.title("ISBN to Excel")

tk.Label(root, text="Enter ISBN:").pack(pady=10)
isbn_entry = tk.Entry(root, width=30)
isbn_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()
