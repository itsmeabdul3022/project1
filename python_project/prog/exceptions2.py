# you can have the user try the input for 4 tries

i = 4
while True:
    try:
        x = int(input("what is x? "))
    except ValueError:
      if i != 0:
       print(f"x is not an integer:remaining tries: {i} ")
       i -= 1
      else:
          print(f"x is not an integer: Remaining tries: {i}")
          break

    else:
        print(f"x is {x}")
        break


""" Using functions:
  def main():
    x = get_int("What's x ? ")
    print(f"x is {x}")


  def get_input(prompt):
      while True:
         try:
             return int(input(prompt))
         except ValueError:
               pass 

   main()
               """
        


