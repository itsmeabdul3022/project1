#find the home for a person based on the input name
# Assumption, A1,A2,A3  lives in H1
# B1 lives in H2
# 

name = input("What's your name: ")
if name == "A1" or name == "A2" or name == "A3":
    print("H1")
elif name == "B1":
    print("H2")
else:
    print("You don't reside here !")

# using match
match name:
      case "A1":
          print("H1")
      case "A2":
          print("H1")
      case "A3":
          print("H1")
      case "B1":
          print("H2")
      case _:
          print("You don't reside here !")
# tighten the above code
match name:
      case "A1" | "A2" | "A3":
          print("H1")
      case "B1":
          print("H2")
      case _:   # - to catch the rest cases
          print("You don't reside here !")

