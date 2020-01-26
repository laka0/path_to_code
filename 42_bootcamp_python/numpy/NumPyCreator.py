import numpy as np

class NumPyCreator():
    
    def from_list(lst, type = float):
        return np.array(lst)
    
    def from_tuple(tpl, dtype = float):
        return np.array(tpl)

    def from_iterable(itr, dtype = float):
        return np.array(itr)

    def from_shape(shape, value = 0, dtype = float):
        return np.full(shape, value)
    
    def random(shape, dtype = float):
        return np.random.random(shape)

    def identity(n, dtype = float):
        return np.identity(n)


npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))
print(type(npc))

print(npc.from_tuple(("a", "b", "c")))

print(npc.from_iterable(range(5)))

#print(npc.from_shape((3, 5)))

#print(npc.identity(4))