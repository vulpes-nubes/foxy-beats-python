import requests
import openpyxl
from openpyxl import Workbook
import tkinter as tk
from tkinter import messagebox

# Function to get book details from Open Library
def get_book_details_open_library(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    data = response.json()
    
    if f'ISBN:{isbn}' in data:
        book_data = data[f'ISBN:{isbn}']
        title = book_data.get('title', 'N/A')
        authors = book_data.get('authors', [])
        year = book_data.get('publish_date', 'N/A')
        
        return title, authors, year
    else:
        return None

# Function to get book details from Google Books API as a fallback
def get_book_details_google_books(isbn):
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(url)
    data = response.json()
    
    if 'items' in data:
        book_data = data['items'][0]['volumeInfo']
        title = book_data.get('title', 'N/A')
        authors = book_data.get('authors', ['N/A'])
        year = book_data.get('publishedDate', 'N/A')
        
        return title, authors, year
    else:
        return None

# Function to create custom reference ID
def create_reference_id(authors, year):
    if authors and isinstance(authors[0], dict) and 'name' in authors[0]:
        author_name = authors[0]['name']
    elif authors and isinstance(authors[0], str):
        author_name = authors[0]
    else:
        return 'N/A'

    last_name, first_name = author_name.split()[-1], author_name.split()[0]
    reference_id = f"{last_name[:3].lower()}-{first_name[:3].lower()}-{year[-4:]}"  # Use last 4 digits of year
    return reference_id

# Function to append or create Excel file
def update_excel(isbn, title, authors, year, reference_id):
    file_name = 'books.xlsx'
    existing_entries = set()

    try:
        wb = openpyxl.load_workbook(file_name)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            existing_entries.add(row[0])  # Assuming ISBN is in the first column
    except FileNotFoundError:
        wb = Workbook()
        sheet = wb.active
        sheet.append(['ISBN', 'Book Title', 'Author(s)', 'Year', 'Reference ID'])

    # Join author names into a single string
    if authors:
        authors_string = ', '.join(author['name'] if isinstance(author, dict) else author for author in authors)
    else:
        authors_string = 'N/A'

    if isbn not in existing_entries:
        sheet.append([isbn, title, authors_string, year, reference_id])
        wb.save(file_name)
        return True, authors_string  # Return authors_string for success message
    else:
        return False, authors_string

# Function to handle ISBN input
def on_submit(event=None):  # Allow event parameter for Enter key
    isbn = isbn_entry.get()
    if isbn:
        # First attempt to get book details from Open Library
        book_details = get_book_details_open_library(isbn)
        if book_details:
            title, authors, year = book_details
        else:
            # Fallback to Google Books API
            book_details = get_book_details_google_books(isbn)
            if book_details:
                title, authors, year = book_details
            else:
                messagebox.showwarning("Error", "No book found for this ISBN.")
                return
        
        # Create custom reference ID
        reference_id = create_reference_id(authors, year)
        
        # Update the Excel file and get authors_string for message
        success, authors_string = update_excel(isbn, title, authors, year, reference_id)
        
        if success:
            messagebox.showinfo("Success", f"Added:\nISBN: {isbn}\nTitle: {title}\nAuthors: {authors_string}\nYear: {year}\nReference ID: {reference_id}")
        else:
            messagebox.showwarning("Duplicate", "This book is already in the list.")
    else:
        messagebox.showwarning("Error", "Please enter an ISBN.")

# Create GUI
root = tk.Tk()
root.title("ISBN to Excel")

tk.Label(root, text="Enter ISBN:").pack(pady=10)
isbn_entry = tk.Entry(root, width=30)
isbn_entry.pack(pady=10)

# Bind the Enter key to the submit function
isbn_entry.bind('<Return>', on_submit)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()
