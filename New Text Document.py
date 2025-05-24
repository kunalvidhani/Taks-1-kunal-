import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
    )

mycursor = db.cursor()

def main_menu():
    while True:
        print("Press 1 for add employee")
        print("Press 2 for veiw employee")
        print("Press 3 for update employee")
        print("Press 4 for delete employee")
        print("Press 5 for exit")
        n=int(input("Enter your choice from 1-5:"))
        if n==1:
            add_emp_details()
        elif n==2:
            veiw_emp_details()
        elif n==3:
            update_emp_details()
        elif n==4:
            delete_emp_details()
        elif n==5:
            print("Thank you for using this")
            brak
        else:
            print("Invalid input")
        
def register():
    username = input("Choose username: ")
    password = input("Choose password: ")
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    try:
        mycursor.execute(query, (username, password))
        db.commit()
        print(" Registered successfully.")
    except:
        print("Username already exists.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    mycursor.execute(query, (username, password))
    result = mycursor.fetchone()
    return result is not None
def add_emp_details():
    name=input("Enter your name:")
    mobile=int(input("Enter your mobile number:"))
    empid=input("Enter your employee id:")
    email= input("Enter your email id:")
    salary=int(input("Enter your salary:"))

    query="insert into ems(name,mobile,empid,email,salary) values(%s,%s,%s,%s,%s)"
    values=(name,mobile,empid,email,salary)
    mycursor.execute(query,values)
    db.commit()
    print("employee details added successfully")
    main_menu()

def veiw_emp_details():
    query="select * from ems"
    mycursor.execute(query)
    data=mycursor.fetchall()
    for i in data:
        print("name=",i[0])
        print("mobile=",i[1])
        print("empid=",i[2])
        print("email=",i[3])
        print("salary=",i[4])
        print("________________________________________")

def update_emp_details():
    emp_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name: ")
    mobile = int(input("Enter new mobile: "))
    email = input("Enter new email  : ")
    salary = float(input("Enter new salary: "))
    query = "UPDATE ems SET name=%s, mobile=%s, email=%s, salary=%s WHERE empid=%s"
    mycursor.execute(query, (name, mobile, email, salary, emp_id))
    db.commit()
    print(" Employee updated successfully.")


def delete_emp_details():
    emp_id = int(input("Enter employee ID to delete: "))
    query = "DELETE FROM ems WHERE empid=%s"
    mycursor.execute(query, (emp_id,))
    db.commit()
    print(" Employee deleted.")


def start():
    print("Welcome to the EMS")
    print("Press 1 for register")
    print("Press 2 for login")
    choice=int(input("Enter your choice:"))
    if choice==1:
        register()
        start()
    if choice==2:
        login()
        print("Login successfully")
        main_menu()
    else:
        print("login failed")
start()