# create a function hello
def hello(to="world"):   # Also assiging a default value to world
    print("hello,", to)
hello()  # this line will print hello world as no arguments are passed to the function
name = input("What's your name? ")
hello(name)


# organizing functions with main at the top and functions down any where , but calling the main function at the bottom

def main():
    name = input("What's your name? ")
    hello(name)
def hello(to="world"):   # Also assiging a default value to world
    print("hello,", to)

main()

# create functions to design the calculator app for square of a number

def main2():
    a = int(input("Enter an interger \n"))
    print(f"Square of a number {a} is {square(a)}")


def square(num):   # function defined for a square 
    return(num * num)

main2()

# scope of variables, the variable name in main function cannot be used in another function.
