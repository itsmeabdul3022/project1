# using dictionaries#  key value pair
students = {
            "A1": "H1",
            "A2": "H1",
            "A3": "H1",
            "B1": "H2"
            }

n = input("Enter the your name \n")
print(f"{n} lives in {students[n]}")

# nested dictionaries  (List of dictionaries)

students2 = [
           {"name": "A1", "house": "H1", "street": "S1",},
            {"name": "A2", "house": "H1", "street": "S1",},
            {"name": "A3", "house": "H1", "street": "S1",},
            {"name": "B1", "house": "H2", "street": "S2",},
    ]
for student in range((len(students2))):
    print(f"{students2[student]["name"]} lives in {students2[student]["house"]} on street {students2[student]["street"]}")

    