# write a lambda fun using filter()
#accept list of numbers and return count of even numbers 
cnt = 0
def Count(No):
    global cnt
    if(No % 2 == 0):
        cnt+=1
    return cnt

CheckEven = lambda NO : list(filter(Count,NO))

def main():
    global cnt
    No = int(input("Number of Element in list :"))
    Data = list()
    print("Enter elemets in List :")

    for i in range(No):
        Element = int(input())
        Data.append(Element)

    print("Elements in list is :",Data)

    CheckEven(Data)
    print("Total Even Numbers is :",cnt)


   
if __name__=="__main__":
    main()