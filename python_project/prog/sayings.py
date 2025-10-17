# user defined libraries locally on the system
import sys

def main():
    hello("world")
    goodbye("world")


def hello(x):
    print(f"Hello, {x}")

def goodbye(y):
    print(f"Goodbye,{y}")

if __name__ == "__main__":   # This is required if the module is called from another program and stop it executing the main function when a function is called.
    main()
