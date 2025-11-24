import mysql.connector as a
con = a.connect (host="localhost",user="root",passwd="12345",database="Digital_Library")
if con.is_connected():
  print("Connected Successfully........")
  print(">>.............................................................................<<")
          
def addbook():
   ti = input("Title : ")
   au = input("Author's Name : ")
   p = input("Publisher : ")
   an = input("Accession No. : ")
   cs = input("Cost of the Book : ")
   s = input("Subject : ")
   tb = input("Total Books : ")
   data = (ti,au,p,an,cs,s,tb)
   mysql = "insert into books values(%s,%s,%s,%s,%s,%s,%s)"
   c = con.cursor()
    c.execute(mysql,data)
    con.commit()
    print(">>......................................................................................<<")
    print("Data Entered Successfully")
   main()

def issueb():
   n = input("Name : ")
   rn = input("Registration No : ")
   an = input("Accession No. : ")
   da = input("Date : ")
   a = "insert into issue values(%s,%s,%s,%s)"
   data = (n,rn,an,da)
   c = con.cursor()
   c.execute(a,data)
   con.commit()
   print(">>........................................................................................<<")
   print("Book issued to : ",n)
   bookup(an,-1)

def submitb():
   n = input("Name : ")
   rn = input("Registration No. : ")
   an = input("Accession No. : ")
   da = input("Date : ")
   a = "insert into submit values(%s,%s,%s,%s)"
   data = (n,rn,an,da)
   c = con.cursor()
   c.execute(a,data)
   con.commit()
   print(">>.......................................................................................<<")
   print("Book Submitted from : ",n)
   bookup(an,1)

def bookup(an,u):
   a = "select Total_Books from books where Accession_No = %s"
   data = (an,)
   c = con.cursor()
   c.execute(a,data)
   myresult = c.fetchone()
   t = myresult[0] + u
   mysql = "update books set Total_Books = %s where Accession_No = %s"
   d = (t,an)
   c.execute(mysql,d)
   con.commit()
   main()

def dbook():
   ac = input("Accession No. : ")
   a = "delete from books where Accession_No = %s"
   data = (ac,)
   c = con.cursor()
   c.execute(a,data)
   con.commit()
   main()

def dispbook():
   a = "select * from books"
   c = con.cursor()
   c.execute(a)
   myresult = c.fetchall()
   for i in myresult:
        print("Title : ",i[0])
        print("Accession No. : ",i[1])
        print("Total Books : ",i[6])
        print(">>...................................................................................<<")
   main()    

def main():
   print("""
                                    


LIBRARY MANAGER

   1. ADD BOOK
   2. ISSUE BOOK
   3. SUBMIT BOOK
   4. DELETE BOOK
   5. DISPLAY BOOKS
   """)
   choice = input("Enter Task No. : ")
   print(">>.....................................................<<")
   if (choice == '1'):
      addbook()
   elif (choice == '2'):
        issueb()
   elif (choice == '3'):
        submitb()
   elif (choice == '4'):
        dbook()
   elif (choice == '5'):
        dispbook()
   else:
         print(" Wrong choice..........")
         main()
def pswd():
   ps = input("Password : ")
   if ps == "pyproject":
       main()
   else:
        print("Wrong Password......")
        pswd()
pswd()
