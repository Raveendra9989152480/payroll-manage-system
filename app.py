from employee import Employee
from employee import SalaryCalculator
from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee_signup', methods=['GET','POST'])
def process_signup():
    if request.method == 'POST':
        employeeId = request.form.get('employeeId')
        employeeName = request.form.get('employeeName')
        departmentId = request.form.get('departmentId')
        designation = request.form.get('designation')
        email = request.form.get('email')
        contactNo = request.form.get('contactNo')
        print(employeeId,employeeName,designation)
        emp = Employee()
        emp.empinsert(EmployeeID = employeeId,Employee_Name=employeeName,DepartmentID= departmentId,Designation=designation,
        Email= email,Contact_No=contactNo)
        print(employeeId)
        return jsonify({'Message':"successfully fetched the data"})
    else:
        return render_template('signup.html')
@app.route('/employees', methods=['GET','POST'])
def show_employees():
    emp=Employee()
    data=emp.show_employees()
    return render_template('showemployees.html',employees=data)
@app.route('/attendance', methods=['GET','POST'])
def attendance():
    if request.method == 'POST':
        departmentId = request.form.get('DepartmentID')
        departmentName= request.form.get('DepartmentName')
        employeeId = request.form.get('EmployeeID')
        employeeName = request.form.get('EmployeeName')
        date = request.form.get('Date')
        timeIn= request.form.get('TimeIn')
        timeOut= request.form.get('TimeOut')
        print(departmentId)
        emp=Employee()
        emp.attendance(DepartmentId=departmentId,DepartmentName=departmentName,EmployeeId=employeeId,EmployeeName=employeeName,Date=date,TimeIn=timeIn,TimeOut=timeOut)
        return jsonify({'Message':"successfully fetched the data"})
    
    return render_template('attendance.html')
@app.route('/payroll_release', methods=['GET','POST'])
def salary():
    if request.method == 'POST':
        employeeId = request.form.get('employeeID')
        departmentId = request.form.get('departmentID')
        accountNo= request.form.get('accountNo')
        pan= request.form.get('PAN')
        basicSalary= request.form.get('basicSalary')
        emp=Employee()
        emp.salary(EmployeeID=employeeId,DepartmentID=departmentId,Account_No=accountNo,PAN=pan,Basic_Salary=basicSalary)
        return jsonify({'Message':"successfully fetched the data"})
    return render_template('salary.html')
@app.route('/attendance_report', methods=['GET','POST'])
def payrollrelease():
    if request.method=='POST':
        eid=request.form.get('employee_id')
        sc=SalaryCalculator()
        total_salary=sc.Salarycalculation(EmployeeID=int(eid))
        context={'EmployeeID':eid,'TotalSalary':int(total_salary)}
        return render_template('showsalary.html',data=context)
    else:
        return render_template('empid.html')




if __name__== '__main__':
    app.run(host='0.0.0.0', port = 5050)

