# using sys.argv
#Prog to print out all the names passed as an argument to the program

import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:  # looping over the list of arguments provided except the first argument at [0] which is the prog name
    print("Hello, my name is", arg)
