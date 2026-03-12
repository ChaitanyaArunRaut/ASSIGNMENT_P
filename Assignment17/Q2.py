def StarPrint(No):
    for i in range(No):
        for j in range(No):
            print("*",end = " ")
        print()
def main():
    Num = int(input("Enter Number of Stars to Print :"))
    StarPrint(Num)

if __name__ == "__main__":
    main()