# using lists
students = ["A1", "A2", "A3"]
print(students)
print(students[0])
print(students[1])

#using for loop

for x in students:
    print(x)

# using numbers in loop

for x in range(len(students)):
    print(students[x])

    print("printing with location",x + 1, students[x])
