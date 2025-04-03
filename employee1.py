#employees = [
 #   {"id": 101, "name": "Alice ", "role": "Manager", "salary": 75000, "department": "HR"},
  #  {"id": 102, "name": "Bob ", "role": "Developer", "salary": 65000, "department": "IT"},
   # {"id": 103, "name": "Charlie ", "role": "Analyst", "salary": 60000, "department": "Finance"}
#]
import json
import os


     #with open('myfile.txt', 'w') as f:  
      #print(record, file=f)

#i = 13
def append_record(record):
    with open('my_file', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

employeecount =int(input("enter the employee count to add"))
print(employeecount)
#while i < employeecount:
for i in range(employeecount):
  name = input("Enter employee name: ")
  #id = input("Enter employee ID: ")
  role = input("Enter employee role: ")
  salary = input("Enter employee salary: ")
  department = input("Enter employee department: ")
  employeeDetails = {"Name": name, "ID": i, "Salary": float(salary), "department": department}
  print(employeeDetails)
  append_record(employeeDetails)

print(employeeDetails)

