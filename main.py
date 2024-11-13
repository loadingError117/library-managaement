#!/usr/bin/env python3

import sqlite3

class library_manager :
    # Variables
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    # Constructor
    def __init__ (self) :
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                       id INTEGER PRIMARY KEY,
                       title TEXT,
                       author TEXT,
                       genre TEXT,
                       year INTEGER)''')
    
    # Adding a book into the library
    def add_book(self, title, author, genre, year) :
        self.cursor.execute("INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)", (title, author, genre, year))
        self.conn.commit()
    
    # View all books in Library
    def view_books(self) :
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        for book in books:
            print(book)
    
    # Serch for a Book
    def search_book(self, keyword) :
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?",
                            ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
        books = self.cursor.fetchall()
        for book in books :
            print(book)
    
    # Update a Book
    def update_book(self, book_id, change_num, update) :
        # Update Title
        if change_num == "1" :
            self.cursor.execute("UPDATE books SET title = ? WHERE id = ?", (update, book_id))
        # Update Author
        elif change_num == "2" :
            self.cursor.execute("UPDATE books SET author = ? WHERE id = ?", (update, book_id))
        # Update Genre
        elif change_num == "3" :
            self.cursor.execute("UPDATE books SET genre = ? WHERE id = ?", (update, book_id))
        # Update Year
        elif change_num == "4" :
            self.cursor.execute("UPDATE books SET year = ? WHERE id = ?", (update, book_id))
        self.conn.commit()
        self.cursor.execute("SELECT * FROM books WHERE id = ?", book_id)
        book = self.cursor.fetchone()
        print(book)

    # Delete a book
    def delete_book(self, book_id) :
        self.cursor.execute("DELETE FROM books WHERE id = ?", book_id)
        self.conn.commit()


def main() :
    manager = library_manager()
    print ("<Library Open>")
    while(True) :
        print("\n<Options>")
        print("1. View all Books")
        print("2. Add a Book")
        print("3. Search for a Book")
        print("4. Update a Book")
        print("5. Delete a Book")
        print("6. Exit")
        select = input("Select: ")
        # View Books
        if select == "1" :
            print("\n<View all Books>")
            manager.view_books()
        # Add a Book
        elif select == "2" :
            print("\n<Add a Book>")
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            year = input("Year: ")
            manager.add_book(title, author, genre, year)
            print(f"<\"{title}\" has been added to the Library>")
        # Search for a Book
        elif select == "3" :
            print("\n<Search for a Book>")
            keyword = input("Search: ")
            manager.search_book(keyword)
        # Update a Book
        elif select == "4" :
            print("\n<Update a Book>")
            manager.view_books()
            id_num = input("ID: ")
            print("\n<Select One>")
            print("1. Title")
            print("2. Author")
            print("3. Genre")
            print("4. Year")
            change_num = input("Select: ")
            enter = input("Enter: ")
            manager.update_book(id_num, change_num, enter)
        # Delete a Book
        elif select == "5" :
            print("\n<Delete a Book>")
            manager.view_books()
            book_num = input("ID: ")
            manager.delete_book(book_num)
            print("\n<Book Deleted>")
        # Exit
        elif select == "6" :
            print("\n<Exit>\n")
            break
        



if __name__ == "__main__" :
    main()