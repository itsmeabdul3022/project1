#intergers
x = int(input("Enter your first number \n"))
y = int(input("Enter your second number \n"))
z = x + y
print(f"The sum of 2 numbers is {z}")

# floating point numbers
x = float(input("Enter your first number \n"))
y = float(input("Enter your second number \n"))
z = x + y
print(f"The sum of 2 numbers is {z}")

#round the result to nearest integer
z = round(x + y)
print(f"The sum of 2 numbers to nearest round is {z}")

#Adding a comma after 3 digits 
print(f"The sum of 2 numbers is {z:,}")

# division
d = round(x / y, 2)
e = x / y 
print(f"The divison of 2 numbers is {d}")
print(f" The divison of 2 numbers rounded to 2 decimals {e:.2f}")

# create functions to design the calculator app for square of a number

def main():
    a = int(input("Enter an interger \n"))
    print(f"Square of a number {a} is {square(a)}")


def square(num):   # function defined for a square 
    return(num * num)

main()




