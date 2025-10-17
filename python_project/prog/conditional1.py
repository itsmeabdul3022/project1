# using conditional statements
# compare the input numbers from users
x = int(input("Enter the number \n"))
y = int(input("Enter the second number \n"))
if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater then {y}")
else:
    print(f"{x} is equal to {y}")

# compare 2 numbers and see if they are equal 
if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")
# grading the student based on the scores

score = int(input("Enter the your score: \n"))
if score >= 90 and score < 100:
    print ("You got grade A")
elif score >= 80 and score < 90:
    print("You got grade B")
else:
    print("You got grade C")

# another way of doing the same
if 90 <= score < 100:
    print("You got grade A")
elif 80 <= score < 90:
    print("You got grade B")
else:
    print("You got grade c")

# ask less questions
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")