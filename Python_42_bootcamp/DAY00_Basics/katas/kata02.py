def date_format(date_tuple):
    print("%d/%d/%d %d:%d" % (date_tuple[3], date_tuple[-1], date_tuple[2], date_tuple[0], date_tuple[1]))

t = (3, 30, 2019, 9, 25)

date_format(t)