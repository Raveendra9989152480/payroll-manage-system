import sqlite3

conn=sqlite3.connect('pms.db')
cur=conn.cursor()
cur.execute('''drop table Employee_Details''')
cur.execute('''drop table Salary_Details''')

cur.execute('''create table Employee_Details (
EmployeeID int primary key,
Employee_Name varchar(50),
DepartmentID int,
Designation varchar(50),
Email varchar(50),
Contact_No int)''')
cur.execute('''create table Salary_Details(
EmployeeID int,
DepartmentID int primary key,
Account_No int,
PAN varchar(50),
Basic_Salary int,
foreign key(EmployeeID) references Employees_Details(EmployeeID)     
)''')
cur.execute('''create table Attendence(
            DepartmentID int ,
            Department_Name varchar(50),
            EmployeeID  int ,
            Employee_Name varchar(50),
            Date datetime,
            Time_In datetime,
            Time_Out datetime,
            foreign key(EmployeeID) references Employee_details(EmployeeID),
            foreign key(DepartmentID) references Salary_details(DepartmentID)
            )''')
conn.commit()
conn.close()
