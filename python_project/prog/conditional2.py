# code to check the parity if the number is even or odd
input1 = int(input("Enter the number \n"))
if input1 % 2 == 0:
    print(f"The given number {input1} is even")
else:
    print(f" The given number {input1} is odd")

# create the same prog using a function that will take a number and return if it is even or odd

def main():
    input2 = int(input("Enter the number"))
    if is_even(input2):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # you can have the same code in one liner
    #   return True if n % 2 == 0 else False
    #or
    #  return ( n % 2 == 0 )
main()