def text_analyzer(text):
    upper_char = 0
    lower_char = 0
    punctuation_char = 0
    spaces = 0

    if len(text) == 0:
        text = input("Please enter a text below \n")
    
    else:
        for i in text: 
            if i.isupper():
                upper_char += 1
            
            elif i.islower():
                lower_char += 1
            
            elif i.isspace():
                spaces += 1
            
            elif i.isnumeric():
                continue
            
            else: 
                punctuation_char += 1
    
    print("The text contains %d upper characters, %d lower characters, %d punctuation characters and %d spaces" % (upper_char, lower_char, punctuation_char, spaces))

    return upper_char, lower_char, punctuation_char, spaces


def main():
    while True:
        user_input = input("1. exit \n2. enter a text to analyse\n")
        if user_input == "exit":
            break
        
        else:
            text_analyzer(user_input)

if __name__ == "__main__":
    main()