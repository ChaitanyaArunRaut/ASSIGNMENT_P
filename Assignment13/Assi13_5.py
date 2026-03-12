# Accept marks and display the Grade
def Grade(No):
    if No >= 75:
        print("Distincton")
    elif No >= 60:
        print("First Class")
    elif No >=50:
        print("Second Class")
    else:
        print("Fail")

def main():
    Marks = 0
    Marks = int(input("Enter the Marks :"))
    Grade(Marks)
if __name__=="__main__":
    main()