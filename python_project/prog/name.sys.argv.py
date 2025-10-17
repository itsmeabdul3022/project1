#use sys module
import sys

#print("Hello, my name is ", sys.argv[1])  # first argument [0] is the name of the file

""" Method1
if len(sys.argv) < 2:
    print("Too few arguments")

elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is ", sys.argv[1])
    """

# Method 2

if len(sys.argv) < 2:
     sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is ", sys.argv[1])




