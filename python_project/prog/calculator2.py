
# create functions to design the calculator app for square of a number

def main():
    a = int(input("Enter an interger \n"))
    print(f"Square of a number {a} is {square(a)}")


def square(num):   # function defined for a square 
    return(num * num)
    
if __name__ == "__main__":
    main()




