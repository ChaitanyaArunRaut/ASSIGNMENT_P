# write a lambda fun. using reduce()
# accept list and return the product of all elements 
from functools import reduce
def Multiplication(No1,No2):
    return No1 * No2

ListProduct = lambda No : int(reduce(Multiplication,No))

def main():
    Value = int(input("Enter number of element :"))
    print("Enter the Elements in List :",)

    Data = list()

    for i in range(Value):
        Elements = int(input())
        Data.append(Elements)

    Result = ListProduct(Data)
    print(Result)

if __name__=="__main__":
    main()