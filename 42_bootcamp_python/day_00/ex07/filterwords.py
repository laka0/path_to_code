def filterwords(string, n):
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    str_list = []
    too_short = []
    punct_clean = list(string)

    for k in punct_clean:
        if k in punct:
            punct_clean.remove(k)
        
    
    str_list = "".join(punct_clean).split()
    print(str_list)
    
    for i in str_list:
        if len(i) <= 3:
            too_short.append(i)
    
    for i in too_short:
        if i in str_list:
            str_list.remove(i)            

    return str_list


print(filterwords("Hello monsieur, ! ça va bien et toi sale pute ?", 3))
