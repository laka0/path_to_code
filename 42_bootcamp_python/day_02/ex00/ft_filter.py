def ft_filter(function, iterable):
    filtered = []
    if function == None:
        for item in iterable:
            if item:
                filtered.append(item)
        
    else:
        for item in iterable:
            if function(item):
                filtered.append(item)

    yield filtered
