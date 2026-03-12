# Create 2 threads nameed evenList and OddList 
# Accept list of the integer
# Evenlist - extract all even element  calculate sum of even
# Oddlist - Extract all odd element and calculate sum of odd
import threading

def EvenList(Num):
    Sum = 0
    for i in Num:
        if (i % 2 == 0):
            print("Even Number is :",i)
            Sum = Sum + i
    print("Sum of Even Numbers :",Sum)

def OddList(Num):
    Sum = 0
    for i in Num:
        if(not i % 2 == 0):
            print("Odd number is :",i)
            Sum = Sum + i
    print("Sum of odd Number is : ",Sum)

def main():
    No = int(input("Enter Numbers you want in list :"))
    Data = list()

    for i in range(No):
        Element = int(input("Enter Numbers in list :"))
        Data.append(Element)

    print("Data in a list : ",Data)

    Even = threading.Thread(target = EvenList,args=(Data, ))
    Odd = threading.Thread(target = OddList,args=(Data, ))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()


if __name__ == "__main__":
    main()