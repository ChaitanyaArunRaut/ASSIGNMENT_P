# write a programe to display 10 to 1 on screen 
def Display(No):
    for i in range(No,0,-1):
        print(i)
def main():
    Num = int(input("Enter Number :"))
    Display(Num)

if __name__ == "__main__":
    main()