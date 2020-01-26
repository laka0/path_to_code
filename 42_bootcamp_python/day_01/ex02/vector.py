class Vector():
    def __init__(self, values):
        self.values = []
        if type(values) == list:
            self.values = values
        
        elif type(values) == int:
            for i in range(values):
                self.values.append(i)
        
        elif type(values) == tuple:
            for i in range(values[0], values[1]):
                self.values.append(i)
        
        else:
            print("Your input is wrong.\nPlease input either a list of vectors, an integer for a size of vector or a tuple for a range of vectors")

        for i in range(len(self.values)):
            self.values[i] = float(self.values[i])
        
        self.size = len(self.values)
    
    def __str__(self):
        msg = "Vector values: " + " ".join(str(self.values)) +"\nVector size: " + str(self.size)
        return msg

    def __add__(self, y):
        added_vector = []
        if type(y) == int or type(y) == float:
            for i in range(self.size):
                added_vector.append(self.values[i] + y)
            print("Normally you can't add a vector with a scallar but i like you so hmm magic !")
        
        elif type(y.values) == list:
            if self.size != y.size:
                print("You can't add two vectors with different sizes")
            else:
                for i in range(self.size):
                    added_vector.append(self.values[i] + y.values[i])
        else:
            print("Error, please add two vectors or a scalar with a vector")
        
        v_add = Vector(added_vector)
        return v_add
    
    def __radd__(self, y):
        return self.__add__(y)
    
    def __sub__(self, y):
        substr_vector = []        
        if type(y) == int or type(y) == float:
            for i in range(self.size):
                substr_vector.append(self.values[i] - y)
            print("Normally you can't substract a vector with a scallar but i like you so hmm magic !")

        elif type(y.values) == list:
            if self.size != y.size:
                print("You can't substract two vectors with different sizes")
            else:
                for i in range(self.size):
                    substr_vector.append(self.values[i] - y.values[i])
        
        else:
            print("Error, please substracte 2 vectors or a vector by a scalar")

        
        v_substr = Vector(substr_vector)

        return v_substr
    
    def __rsub__(self, y):
        print("You can't substract a scalar by a vector")
    
    def __mul__(self, y):
        if type(y) == int or type(y) == float:
            scalar_mul_vector = []
            for i in range(self.size):
                scalar_mul_vector.append(self.values[i] * y)
            
            scal_vector = Vector(scalar_mul_vector)
            return scal_vector

        elif type(y.values) == list:
            if self.size != y.size:
                print("You can't multiply two vectors with different sizes")
            else:
                mul_vector = 0
                for i in range(self.size):
                    mul_vector += self.values[i]*y.values[i]
                return mul_vector
        
        else:
            print("Error, please multiply 2 vectors or a vector by a scalar")

        
        
    
    def __rmul__(self, y):
        return self.__mul__(y)

    
    def __truediv__(self, y):
        if y == 0:
            print("Error, division by zero")
        
        elif type(y) == int or type(y) == float:
            return self.__mul__(1/y)
        else:
            print("Error, please divide a vector by a scalar")
    
    def __rtruediv__(self, y):
        print("Can't divide by a vector")
    
    def __repr__(self):
        return (f'<Vector object at {hex(id(self))}>')

