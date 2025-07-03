class Employee_details:
    def department(self):
        dep_list=[]
        x=int(input("enter the number of department you have to add:"))
        for i in range(x):
            d=input("enter the department:")
            dep_list.append(d)
        return dep_list
    def job_title(self):
        job_list=[]
        y=int(input("enter the number of jobs you have to add:"))
        for i in range(y):
            z=input("enter the job:")
            job_list.append(z)
        return job_list
class Employee:
    emp_dict={}
    def __init__(self,ename,dep,job):
        self.ename=ename
        self.dep=dep
        self.job=job
    def add_emp(self):
        self.emp_dict[self.ename]={'name':self.ename,'department':self.dep,"job_title":self.job}
        print("AADDDEEDDD SUUUCCCEESSSFFFULLLYYY>........")
    def view_emp(self):
        ch=int(input("1.VIEW ALL EMPLOYEES\n2.VIEW SINGLE EMPLOYEE\nENTER YOUR CHOICE:"))
        if ch==1:
            print(self.emp_dict)
        elif ch==2:
            x=input("enter the employee name you have to view:")
            if x in self.emp_dict:
                print(self.emp_dict[x])
            else:
                print("EMPLOYEE DOES NOT EXIST")
        else:
            print("invalid choice")
    def update_emp(self):
        x=input("Enter the employee you have to update:")
        if x in self.emp_dict:
            print(self.emp_dict[x])
            ch=int(input("1.UPDATE NAME\n2.UPDATE DEPATMENT\n3.UPDATE JOB TITLE\n ENTER YOUR CHOICE:"))
            if ch==1:
                new_name=input("ENter the new name:")
                pop=self.emp_dict.pop(x)
                self.emp_dict[new_name]=pop
                self.emp_dict[new_name]['name']=new_name
                print(self.emp_dict[new_name])
            elif ch==2:
                z=int(input("Enter the position of the department you have to update:"))
                up=z-1
                y=input("Enter the new department")
                self.emp_dict[x]['department'][up]=y
                print(self.emp_dict[x]['department'])
            elif ch==3:
                z=int(input("enter which position of job ttile you have to update:"))
                up=z-1
                y=input("enter the new job title:")
                self.emp_dict[x]['job_title'][up]=y
                print(self.emp_dict[x]['job_title'])
            else:
                print("INVALID CHOICE.............")
        else:
            print("Employeee doesnot exist")
    def emp_dlt(self):
        x=input("enter the employee you have to delete")
        if x in self.emp_dict:
            print(self.emp_dict[x])
            ch=int(input("1.DLT NAME\n2.DLT DEPARTMENT\n3.DLT JOBTITLE\nENTER YOUR CHOICE:"))
            if ch==1:
                del self.emp_dict[x]
                print(self.emp_dict)
            elif ch==2:
                print(self.emp_dict[x]['department'])
                z=int(input("Enter the position of the department you have to dlt"))
                pop=z-1
                del self.emp_dict[x]['department'][pop]
                print(self.emp_dict[x]['department'])
            elif ch==3:
                print(self.emp_dict[x]['job_title'])
                y=int(input("Enter the position of job title you have to dlt"))
                pop=y-1
                del self.emp_dict[x]['job_title'][pop]
                print(self.emp_dict[x]['job_title'])
            else:
                print("INVALID CHOICEEE......")
        else:
            print("EMPLOYEE does not EXIST")
while True:
    choice=int(input("1.ADD EMPLOYEE\n2.VIEW EMPLOYEE\n3.UPDATE EMPLOYEE\n4.DELETE EMPLOYEE\n5.EXIT\nENTER YOUR CHOICE"))
    if choice==1:
        name=input("Enter the employee NAME:")
        emp=Employee_details()
        d_list=emp.department()
        j_list=emp.job_title()
        e=Employee(name,d_list,j_list)
        e.add_emp()
    elif choice==2:
        e.view_emp()
    elif choice==3:
        e.update_emp()
    elif choice==4:
        e.emp_dlt()
    elif choice==5:
        break
    else:
        print("invalid choice")

