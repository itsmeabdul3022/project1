name = input("What's your name \n")

#print(*objects, sep='' , end='\n',file=sys.stdout, flush=False)
#By default, the arguments are seperated by space. Print function ends with \n. We can overwrite with end=""

print("hello, ")
print(name)

# format
print("Hello, ", end="")
print(name)


print("Hello," + name)

# second syntax using comma 
print("Hello,", name)

#print with another seperator
print("Hello,", name , sep="?")

#escape characters
print("Hello, \"name\"")
