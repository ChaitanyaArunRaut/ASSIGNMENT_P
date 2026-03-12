# Display 

def Display(No):
    for i in range(1, No+1, 1):
        for j in range(1, i+1, 1):
           print(j,end = " ")
        print()


def main():

    value = int(input("Enter Number of "))
    Display(value)

if __name__ == "__main__":
    main()
    