import openpyxl as xl

class Employee:
    id = ''
    name = ''
    job_title = ''
    salary = 0
    def __init__(self, id, name, job_title, salary):
        self.id = id
        self.name = name
        self.job_title = job_title
        self.salary = salary

e1 = Employee('123', 'Fatoom', 'CS Engineer', 20000)
e2 = Employee('222', 'Hanan', 'Pharmacy Lead', 30000)
e3 = Employee('233', 'Eman', 'Manager', 50000)
e4 = Employee('444', 'Basma', 'Team Lead', 20000)
employees = [e1, e2, e3, e4]

wb = xl.Workbook()
ws = wb.active
ws.append(('ID','Name','Job Title','Salary'))

for employee in employees:
    ws.append((employee.id, employee.name, employee.job_title, employee.salary))

wb.save('C:/Users/Fatoom/Documents/employees.xlsx')


