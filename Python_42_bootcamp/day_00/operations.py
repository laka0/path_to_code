def operations(x, y):
    print("Sum: %d \nDifference: %d\n Product: %d\n Quotient: %d\n Remainder: %d" % (x+y, x-y, x*y, x/y, x%y))

    return x+y, x-y, x*y, x/y, x%y

def main():
    while True:
        user_input = input("1. exit\n 2. Enter 2 numbers")

        if user_input =="exit":
            break

        else:
            x, y = 
            operations(user_input)