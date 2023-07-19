import sqlite3


class Employee:
    def empinsert(self,**k):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''
        insert into Employee_Details
        values ({k['EmployeeID']},
        "{k['Employee_Name']}",
        {k['DepartmentID']},
        "{k['Designation']}",
        "{k['Email']}",
        {k['Contact_No']})
        ''')
        conn.commit()
    

    def show_employees(self):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute('''select * from Employee_Details''')
        data=[]
        for i in cur.fetchall():
            context={}
            context['EmployeeId']=i[0]
            context['EmployeeName']=i[1]
            context['DepartmentId']=i[2]
            context['Designation']=i[3]
            context['Email']=i[4]
            context['ContactNo']=i[5]
            data.append(context)
        return data
    def attendance (self,**k):
        conn= sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''insert into Attendence
            values({k['DepartmentId']},
            "{k['DepartmentName']}",
            {k['EmployeeId']},
            "{k['EmployeeName']}",
            "{k['Date']}",
            "{k['TimeIn']}",
            "{k['TimeOut']}") ''')
        conn.commit()
    def salary (self,**k):
        conn= sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f'''insert into Salary_Details
            values({k['EmployeeID']},
            {k['DepartmentID']},
            {k['Account_No']},
            "{k['PAN']}",
            {k['Basic_Salary']}
            )''')
        conn.commit()
    