class Employee:
    def __init__(self, empno, name, deptname, desig, age, salary):
        self.empno=empno
        self.name=name
        self.deptname=deptname 
        self.desig=desig
        self.age=age
        self.salary=salary

    def display(self):
        print( self.empno +" "+ self.name+" "+ self.deptname+" "+ self.desig+" "+ self.age+" "+ self.salary)
    
    def search(self,eno):
        if self.empno==eno:
            return True
        else:
            return False

elist=list()
n = int(input("Enter number of Employees :"))
print("Employee Details Entry. ")
print("_______________________________________________________")
for i in range(n):
    empno=input("Enter the Employee number : ")
    name=input("Enter the Employee name : ")
    deptname=input("Enter the Department name :")
    desig= input("Enter the Designation : ")
    age=input("Enter the age : ")
    salary=input("Enter the Salary : ")
    elist.append(Employee(empno, name, deptname, desig, age, salary))
print("_______________________________________________________")
print("........Employee Information....... ")
for i in range(n):
    elist[i].display()
print(".......Search.......")
n=input("Enter the employee number :")
for e in elist:
    found=e.search(n)
    if found:
        e.display()
        break
    else:
        print("Employee not found")
        