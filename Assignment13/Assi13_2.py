# print the Radius of circle
def AreaCircle(Value):
    Ans = 0.0
    PI = 3.14159
    Ans = PI * Value*Value
    return Ans
def main():
    Radius = float(input("Enter the radious of the circle :"))
    Ret  = 0
    Ret = AreaCircle(Radius)
    print("Area of Circle is :",Ret)
    
if __name__=="__main__":
    main()