import sqlite3

def show_employee(self):
    conn=sqlite3.connect('pms.db')
    cur=conn.cursor()
    cur.execute('''select * from Employee_Details''')
    data=[]
    for i in cur.fetchall():
        context={}
        context['EmployeeID']=i[0]
        context['EmployeeName']=i[1]
        context['DepartmentID']=i[2]
        context['Designation']=i[3]
        context['Email']=i[4]
        context['ContactNo']=i[5]
        data.append(context)
    return data

from employee import Employee
emp=Employee()
emp.attendance(DepartmentId=1,DepartmentName='ece',EmployeeId=1,EmployeeName='ravi',Date='12/6/2001',TimeIn='09:30',
               TimeOut='05:30')
