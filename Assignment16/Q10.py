# Accept Name from user and print its length.
def NameLength(name): 
    Lenght = 0
    for i in name:
        Lenght = Lenght + 1
    print("Lenght of Name is :",Lenght)

# using inbuild function
def name_lenght(name):
    print("Length of Name is :",len(name))
def main():
    Name = input("Enter your Name :")
    NameLength(Name)
    name_lenght(Name)


if __name__ == "__main__":
    main()