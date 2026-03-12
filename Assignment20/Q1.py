# Design a Python application that creats two separate threads named Even and ODD
# Even Thread Display first 10 even numbers.
# Odd Thread Display First 10 Odd numbers . Using threading module.
import threading
def CheckEven():
    Cnt = 0
    i = 1
    while(Cnt < 10):
        if(i % 2 == 0):
            print(i,end= " ")
            i = i + 2
            Cnt = Cnt + 1
        else :
            i = i + 1
    print()

def CheckOdd():
    Cnt = 0
    i = 1
    while(Cnt < 10):
        if(not(i % 2 ==0)):
            print(i, end = " ")
            i = i + 2
            Cnt = Cnt + 1

        else:
            i = i +1
    print()

def main():
    Even = threading.Thread(target = CheckEven)
    Odd  = threading.Thread(target = CheckOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()
