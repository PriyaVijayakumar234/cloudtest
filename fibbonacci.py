#def fibbo(n):
 #   a=0
  ##  b=1
    #c=1
    #if n>=c:
     #   for i in range(n):
      #      print(a)
       #     print(b)
        ##   a=b+c
          ##  b=c+a
            #c=a+b  
    

#def fibR(n):
 #if n==1 or n==2:
  #return 1
 #return fibR(n-1)+fibR(n-2)

def sum(num1, num2):
    return num1 + num2


def sum_only_positive(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 + num2
    else:
        return None
    
#print("displaying fibbonacci series")
n=int(input("enter the number1:"))
n1=int(input("enter the number2:"))
#fibR(n)
#fibbo(n)
sum(n,n1)
sum_only_positive(n,n1)
print("end of the program")
# Compare this snippet from test.py:
