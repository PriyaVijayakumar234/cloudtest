empList=["priya","Senthil","vasanthi","senthil","priya"]
positionList=list["Manager","Developer","Tester","Developer","Manager"]

newpositionList=["Manager","Developer","Tester","Developer","Manager"]
print(empList)
print(list(enumerate(empList)))
print("size list:" ,len(empList))
print(type(empList))
print("list of positions:",positionList)
empList.insert(4,"reena")
empList[4:6]=["sushma","vasavi"]
newpositionList.insert(4,"designer")
print(empList)
print(newpositionList)