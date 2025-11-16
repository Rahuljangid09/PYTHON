# Simple Calculator

Num1=int(input('Enter Value 1:'))
Num2=int(input('Enter value 2:'))
Opr=input("Enter operation:")

if Opr=="+":
    print(Num1+Num2)
elif Opr=="-":
    print(Num1-Num2)    
elif Opr=="*":
    print(Num1*Num2)    
elif Opr=="/":
    print(Num1/Num2) 
else:
    print('invalid opr') 
         