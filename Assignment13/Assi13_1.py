# accept the length and width of rectangle and print area.
def AreaRectangle(Len, wid):
    Area = 0.0
    Area = Len * wid
    return Area

def main():
    Length = float(input("Enter the Length :"))
    Width = float(input("Enter the Width :"))
    Ret = 0

    Ret = AreaRectangle(Length, Width)
    print("Area of Rectangle is :",Ret)

if __name__=="__main__":
    main()
