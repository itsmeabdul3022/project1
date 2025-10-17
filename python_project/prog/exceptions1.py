#exceptions in python
try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
      print("x is not an integer")

# The better strategy is to handle the exception and print the number if no error
""" 
try:
    x = int(input("What is x? "))   
except ValueError:
      print("x is not an integer")
else:
     print(f"x is {x}")
      """

# ideally use While loop and have the user input correct number

while True:
    try:
      x = int(input("What is x? "))   
    except ValueError:
      print("x is not an integer")
    else:
        break
print(f"x is {x}")


