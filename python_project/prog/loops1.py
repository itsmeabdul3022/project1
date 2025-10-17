#loops using while print hello 3 times
i = 3
while i != 0:
    print("Hello")
    i =  i - 1


i = 0
while i < 3:
    print("Hello using another method")
    i += 1  # same as i = i + 1

# using for
for x in [0,1,2]:
    print("Hello using for loop")

    # using range in for loop
for x in range(3):
    print("Hello using range in loop")
# Note: You can use for _ in range(3):    If you not using the variable anywhere in the prog
# Achieving the same without loops but using *
print("Hello using *\n" * 3, end="")