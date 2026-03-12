import Arithmatic

print("Inside client ",__name__)
print("Value of  PI is :",Arithmatic.PI)

print("_"*20)

Result = 0
Result = Arithmatic.Add(int(input("Enter first Number :")),int(input("Enter Second Number :")))
print("Addition is :",Result)

print("_"*20)

Result = Arithmatic.Sub(int(input("Enter first Number :")),int(input("Enter Second Number :")))
print("Substraction is :",Result)

print("_"*20)

Result = Arithmatic.Mul(int(input("Enter first Number :")),int(input("Enter Second Number :")))
print("Multiplication is :",Result)

print("_"*20)

Result = Arithmatic.Div(int(input("Enter first Number :")),int(input("Enter Second Number :")))
print("Division is :",Result)