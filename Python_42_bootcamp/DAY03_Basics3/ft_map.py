def ft_map(function, *inputs):
    mapped = []
    for i in range(len(inputs)):
        mapped.append([])
        for k in range(len(min(inputs, key = len))):
            mapped[i].append(function(inputs[i][k]))
    
    return mapped

def square(x):
    return x*x

l1 = [2, 3, 4]
l2 = [10, 11, 12, 13]

print(ft_map(square, l1, l2))