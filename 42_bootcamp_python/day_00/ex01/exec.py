def rev_alpha(string):
    new_string = []

    for i in range(1, len(string)+1):
        new_string.append(string[-i].upper())

    return "".join(new_string)

def main():
    while True:
        user_input = input("1. Type exit \n2. Type a string to reverse  ")
        if user_input == "exit":
            break

        else:
            print(rev_alpha(user_input))


if __name__ == "__main__":
    main()