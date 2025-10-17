# Hello using functions
# It is better to have hello function to return a value rather than printing as it will make it easy to write a unit test for the function.
def main():
    name = input("What is your name ? ")
    output = hello(name)
    print(output)

def hello(to="world"):
   # print("Hello ", to)   # better to have return value like in next line
    return f"hello, {to}"

if __name__  == "__main__":
    main()
