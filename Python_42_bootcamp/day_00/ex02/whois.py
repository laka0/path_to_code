def whois(x):
    try:
        x = int(x)
    except ValueError:
        print("ERROR")
        return False

    if x == 0:
        print ("I'm Zero.")
        
    elif x % 2 == 0:
        print("I'm Even.")
        
    else:
        print("I'm Odd.")

def main():
    while True:
        user_input = input("1. exit \n2. enter a valid integer\n")
        if user_input == exit:
            break
        
        else:
            whois(user_input)

if __name__ == "__main__":
    main()
