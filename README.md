Project Title:
Library Management System

Overview Of Project:
The library management system is to operate a library with efficiency and at reduced costs. The system being entirely automated streamlines all the tasks involved in operations of the library. The activities of book purchasing, cataloging, indexing, circulation recording and stock checking are done by the software. Such software eliminates the need for repetitive manual work and minimizes the chances of errors.

The library management system software helps in reducing operational costs. Managing a library manually is labor intensive and an immense amount of paperwork is involved. An automated system reduces the need for manpower and stationery. This leads to lower operational costs.


The system saves time for both the user and the librarian. With just a click the user can search for the books available in the library. The librarian can answer queries with ease regarding the availability of books. Adding, removing or editing the database is a simple process. Adding new members or cancelling existing memberships can be done with ease.

Stock checking and verification of books in the library can be done within a few hours. The automated system saves a considerable amount of time as opposed to the manual system.

The library management system software makes the library a smart one by organizing the books systematically by author, title and subject. This enables users to search for books quickly and effortlessly.

Students need access to authentic information. an advanced organized library is an integral part of any educational institution. In this digital age a web based library management system would be ideal for students who can access the library’s database on their smart phones.

Feactures:
1. Add Books
Allows entering complete book details into the MySQL database.

2. Issue Books
Issues a book to a student and reduces the Total_Books count automatically.

3. Submit Books
Records book return and increases the Total_Books count.

4. Delete Books
Removes a book record using its Accession Number.

5. Display Books
Shows all books with title, accession number, and available quantity.

6. Automatic Book Quantity Update
Updates the stock whenever a book is issued or submitted.

7. Password Protection
Only authorized users can access the system.

8. User-Friendly Menu
Simple menu-driven interface for easy use.

9. MySQL Database Storage
All data is stored safely and updated in real time.

Technologies used:
Programming language - Python3.X
Arora, Sumita.Computer Science, XI. Delhi:Dhanpat Rai & Co.
Arora, Sumita.Computer Science, XII. Delhi:Dhanpat Rai & Co.
Youtube Chennels: https://www.w3schools.com/MySQL/default.asp
                  https://www.youtube.com/watch?v=mt-5FGkw2zY

Steps to install & run the project:
1. Install Required Software
Install Python.
Install MySQL Server + MySQL Workbench.
Install MySQL connector in Python

2. Create Database in MySQL
Open MySQL Workbench and run

3. Update Connection Details (if needed)
Make sure your Python code has correct MySQL credentials 

4. Run the Project
Save your code as library.py
Open CMD/Terminal and run
Enter password

5. Use the Menu
1 → Add Book
2 → Issue Book
3 → Submit Book
4 → Delete Book
5 → Display Books

Instructions for Testing:
1. Start the Program
Run your Python file

2. Enter Password
Use the login password

3. Test Each Feature
A. Test Add Book
Choose 1 from the menu.
Enter book details.
Check MySQL table books to confirm the data is added.
B. Test Issue Book
Choose 2.
Enter student name, reg no, accession no, date.
Check issue table for new entry.
Check books.Total_Books decreased by 1.
C. Test Submit Book
Choose 3.
Enter same book accession no.
Check submit table for entry.
Ensure Total_Books increased by 1.
D. Test Delete Book
Choose 4.
Enter accession number.
Check if the record is removed from books table.
E. Test Display Books
Choose 5.
Verify all books are printed correctly.

4. Test Wrong Inputs
Enter wrong task number.
Enter wrong password.
Check if program handles errors properly.

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
