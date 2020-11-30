def generator(text, sep = " ", option=None):
    str_generator = text.split(sep)

    if type(text) != str:
        print("Error: your text is not a string")
    elif option == None:
        yield str_generator
    elif option == "shuffle":
        pass

    elif option == "unique":
        unique_words = []
        for i in range(len(str_generator)):
            if str_generator[i] not in unique_words:
                unique_words.append(str_generator[i])
        yield unique_words

    elif option == "ordered":
        str_generator.sort()
        yield str_generator
    else:
        print("Error: not a valid option.\n Please choose between shuffle, unique or ordered")

msg = "Le lorem ipsum ipsum est simplement du faux texte et est du fromage"
for i in generator(msg):
    print(i)