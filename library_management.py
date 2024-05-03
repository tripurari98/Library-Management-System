import mysql.connector as a
con=a.connect(host='localhost',username='root',password='nath@98',database='library')
# print(" Data base successfully connected ")

def addbook():
    book_name=input("Enter The Book Name : ")
    book_author=input("Enter The Author's Name : ")
    book_code=int(input("Enter The Book Code : "))
    total=int(input("Total Books : "))
    sub=input("Enter Subject : ")
    data=(book_name,book_author,book_code,total,sub) # create a tuple 

    sql='insert into books values(%s,%s,%s,%s,%s);' # insert data into books table 
    c=con.cursor()   # create a cursor object a . it is use to execute SQL Commands
    c.execute(sql,data) # execute the sql query
    con.commit()       # commits the transaction to the database.
    print("\n\n Book Added Successfully.....\n")
    wait=input('\n Press enter to continue...\n')  # wait for the user
    main()
 
def issue_book():
    student_name=input("Enter The Student Name : ")
    en_no=input("Enter Enrollment No. : ")
    co=int(input("Enter Book Code : "))
    date=input("Enter Date : ")
    a='insert into issue values(%s,%s,%s,%s);'
    data=(student_name,en_no,co,date)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("\n Book issued Successfully :")
    wait=input("\n Press enter to continue...\n")
    main()


def return_book():
    student_name=input("Enter Student Name : ")
    en_no=input("Enter Enrollment No : ")
    co=input("Enter Book Code : ")
    date=input("Enter Date : ")
    a="insert into return_ values(%s,%s,%s,%s);"
    data=(student_name,en_no,co,date)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book Return by :",student_name)
    wait=input('\n\npress enter to continue...\n\n')

    main()

def dbook():
    ac=int(input("Enter Book Code : "))
    a="delete from books where Book_code=%s;"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("\nBook Deleted Successfully : ")
    wait=input("\n Press enter to continue...\n\n")
    main()


def dispbook():
    a="select*from books;"
    c=con.cursor()
    c.execute(a)  #   executes the SQL query stored in the variable a
    myresult=c.fetchall() # This line fetches all the rows 
    for i in myresult:
        print("Book Name :",i[0]) # prints the value of the first column (index 0) of the current row
        print("Author : ",i[1])
        print("Book Code :",i[2])
        print("Total : ",i[3])
        print("Subject :",i[4])
        print("\n")
    wait=input('\n press enter to continue ...\n')
    main()

def report_issued_books():
    a="select*from issue;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(i)
    wait=input("\npress enter to continue ...\n")
    main()
def report_return_books():
    a="select*from return_;"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print(i)
    wait=input("\n press enter to continue...\n")
    main()


def report_menu():
    print('''REPORT MENU
---------------
    1. ISSUED BOOKS
    2. RETURNED BOOKS
    3. GO BACK TO MAIN MENU\n''')
    choice = input("Enter Task No:... ")
    print("\n\n")
    if choice == '1':
        report_issued_books()
    elif choice == '2':
        report_return_books()
    elif choice == '3':
        main()
    else:
        print("Invalid choice. Please try again...\n")
        report_menu()

def main():
    print(''' \n\n LIBRARAY MANAGEMENT SYSTEM
-----------------------------

             1. ADD BOOK
             2. ISSUE OF BOOK
             3. RETURN OF BOOK
             4. DELETE BOOK
             5. DISPLAY BOOKS
             6. REPORT MENU
             7.EXIT PROGRAM
    ''')
    choice=input("Enter Task No:...")
    print('\n')
   
    if(choice=='1'):
       addbook()
    elif(choice=='2'):
      issue_book()
    elif(choice=='3'):
      return_book()
    elif(choice=='4'):
      dbook()
    elif(choice=='5'):
      dispbook()
    elif(choice=='6'):
         report_menu()
 
    elif (choice=='7'):
         print(' Thank you and have a great day ahead...\n')
    else:
        print(" Invalid choice ! Please try again...\n")
        main()
main()




