Problem Statement:
The purpose of this project is to develop a Library Management System using Python and MySQL that helps automate basic library operations. The system should allow the librarian to add new books, issue books to students, submit returned books, delete books, and display available books. It should also maintain accurate records in the database and automatically update the total number of books when books are issued or returned. The system must be simple, menu-driven, password-protected, and interact with the MySQL database for storing and managing all library data efficiently.

Scope for the Project:
The Library Management System aims to simplify and digitalize basic library operations using Python and MySQL. The scope of this project includes:
Storing book details such as title, author, publisher, subject, accession number, and total copies.
Issuing books to students and updating the available stock automatically.
Submitting/returning books and increasing the total book count accordingly.
Deleting book records from the database when required.
Displaying all books stored in the library database.
Password-protected access to ensure authorized use.

Menu-driven interface for easy interaction and smooth operation.The system focuses on basic library functionalities and is suitable for small libraries, schools, or academic projects.

Target users:
Librarians – to manage book records, issue books, and track submissions easily.
School/College Students – to borrow and return books efficiently.
Teachers and Staff – to access and manage library resources.
Small Libraries – ideal for small institutions needing a simple, menu-based management system.
Beginner Programmers/Students – useful for learning Python–MySQL integration and basic database operations.

High-level Features:
1. Book Management
Add new books with details like title, author, publisher, accession number, cost, subject, and total copies.
Delete books using accession number.
Display all books stored in the database.

2. Issue Book Functionality
Issue a book to a student by recording:
Student name
Registration number
Accession number
Date of issue
Automatically reduces the total number of available copies.

3. Submit/Return Book Functionality
Submit a return entry with:
Student name
Registration number
Accession number
Date of return
Automatically increases the total number of available copies.

4. Book Stock Update System
Updates the number of available books whenever a book is issued or submitted.
Prevents manual counting errors.

5. Password Protection
Provides a basic password check before accessing the main menu.
Prevents unauthorized access to library operations.

6. Interactive Menu-Driven System
Simple text-based menu for:
1. Add Book
2. Issue Book
3. Submit Book
4. Delete Book
5. Display Books
Repeats the menu after every operation for smooth workflow.

7. MySQL Database Integration
Stores and retrieves all data using MySQL tables:
books
issue
submit
Ensures permanent and reliable data storage.
