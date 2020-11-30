class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = int(cooking_lvl)
        self.cooking_time = int(cooking_time)
        self.ingredients = ingredients.split()
        self.description = description
        self.recipe_type = recipe_type
    
    def __check_values__(self):
        #Name
        while True:
            if len(self.name) == 0:
                self.name = input("Error: the name is blank.\nPlease enter another name below\n")
            else:
                break
        #Cooking Level
        while True: 
            try:
                self.cooking_lvl + 2 
            except ValueError:
                 self.cooking_lvl = int(input("Error : you did not enter a number.\nPlease put a rate between 0 to 5 for the cooking level\n"))
            if self.cooking_lvl < 1 or self.cooking_lvl > 5:
                self.cooking_lvl = int(input("Error: you entered a number out of range 1 to 5.\nPlease put a rate between 0 to 5 for the cooking level\n"))
            else:
                break
        #Cooking time
        while True:
            try:
                self.cooking_time + 2
            except ValueError:
                self.cooking_time=  int(input("Error : you did not enter a number.\nPlease put a cooking time in minutes\n"))
            if self.cooking_time < 0:
                self.cooking_time = int(input("Error: you put a negative number. \n Please enter another one for the cooking time.\n"))
            else:
                break

        #Ingredients
        while True:
            if len(self.ingredients) == 0:
                self.ingredients = input("Error: ingredients are missing\nPlease enter your ingredients below").split()
            else:
                break
        
        #Recipe type
        while True:
            type_recipe = ["starter", "lunch", "dessert"]

            if self.recipe_type not in type_recipe: 
                self.recipe_type = input("Error: your recipe type does not exist.\nPlease choose below between starter, lunch or dessert")

            else:
                break
        
        print("No errors")

    def  __str__(self):
        # Return the string to print with the recipe info

        txt = ""

        txt += "Name: %s\n" % self.name
        txt += "Cooking difficulty: %s\n" % self.cooking_lvl
        txt += "Cooking time : %s\n" % self.cooking_time
        txt += "Ingredients: %s\n" % self.ingredients
        txt += "Description: %s\n" % self.description
        txt += "Recipe type: %s\n" % self.recipe_type

        return txt
    

pizza = Recipe("pizza", 3, 45, "pate tomate jambon", "", "lunch")
pizza.__check_values__()
print(pizza.__str__())

