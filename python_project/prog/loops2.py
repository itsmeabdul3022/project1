#using continue and break in loops
while True:
    n = int(input("What's n?"))
    if n < 0:
        print("Please enter valid number ")
        continue
    else:
        break
for _ in range(n):
    print("Hello using while and for")

# same prog using functions to get number and print hello

def main():
     number = get_number()
     Hello(number)

def get_number():
    while True:
        n = int(input("Enter the number \n"))
        if n < 0:
            print("Enter a valid number \n")
            continue
        else:
            return n
            break  # you can delete break line 

def Hello(num):
    for _ in range(num):
        print("Hello using functions")

main()
