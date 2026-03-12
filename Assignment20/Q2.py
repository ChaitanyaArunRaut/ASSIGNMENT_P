# Design a python application that creats two threads named EvenFactor and OddFactor
# Both Thread accept one integer number as parameter
# EvenFactor - Identify all even factors of the given number and calculate and display the sum of the even factors
# OddFactor - identify odd factor calculate and display the sum of odd factors


import threading
def EvenFact(Num):
    Sum = 0
    for i in range(1, Num // 2 +1):
      if(Num % i == 0):
        if(i % 2 == 0):
          Sum = Sum + i 
    print("Additon of Even Factors :",Sum)

def OddFact(Num):
    Sum = 0
    for i in range(1,Num // 2, +1):
      if(Num % i == 0):
        if(not(i % 2 == 0)):
          print(i)
          Sum = Sum + i
    print("Additon of Odd Factors : ",Sum)

def main():
  value = int(input("Enter Number :"))
  Even = threading.Thread(target = EvenFact,args=(value, ))
  Odd = threading.Thread(target = OddFact,args=(value, ))

  Even.start()
  Odd.start()

  Even.join()
  Odd.join()

  
if __name__ == "__main__":
  main()