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

#escape character
print("Hello, \"", name )

#print with another seperator
print("Hello,", name , sep="?")

# format string

print(f"Hello, {name}")

# printing with cleaning up user input with spaces . strip will remove spaces from the begining and end of the line and not in between
name = name.strip()
print(f"Hello,", name)

# capaitalize will capitalize first letter of a line
name = name.capitalize()

print(f"Hello,", name)

# title will capitalize first letters in a line
name = name.title()

print(f"Hello", name)

#joining 2 functions
name = name.strip().title()

print(f"Hello,", name)

# we can combine with input command

name = input("Enter your name \n").strip().title()
print(f"Hello,", name)

#split user's name into first name and last name with a space
first, last = name.split(" ")

print(f"Hello, {first}")


