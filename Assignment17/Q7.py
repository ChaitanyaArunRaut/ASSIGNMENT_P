# Display 

def Display(No):
    for i in range(No):
        for j in range(No):
           print(j+1,end = " ")
        print()



def main():

    value = int(input("Enter Number of "))
    Display(value)

if __name__ == "__main__":
    main()
    