# program to use functions to print rows and columns of square

def main():
    print_square(3)

def print_square(size):
    for x in range(size):
        print ("#" * size)
""" or can use
def print_square(size):
for i in range(size):
    for j in range(size):
        print("#", end="")
  print()""" 

main()
