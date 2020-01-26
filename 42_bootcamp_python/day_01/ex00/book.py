import re 

class Book:
    def __init__(self, name, last_update, creation_date):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {
            "starter": {},
            "lunch": {},
            "dessert": {},}

    def __check_values__(self):
        #Name
        while True:
            if len(self.name) == 0:
                self.name = input("Error: the name is blank.\nPlease enter another name below\n")
            else:
                break
        
        # last_update 
        date_regex = re.compile(r'\d\d/\d\d/\d\d\d\d')

        while True:
            if date_regex.search(self.last_update) == None:
                self.last_update = input("Error : wrong date format. \nPlease enter below a new last update date with thhis format: 16/10/2018\n")

            else: 
                break
        
        # creation_update
        while True:
            if date_regex.search(self.creation_date) == None:
                self.creation_date = input("Error : wrong date format. \nPlease enter below a new creation update date with thhis format: 16/10/2018\n")

            else: 
                break
        
        print("No errors")

recipe_book = Book("La cocina de mama", "15/01/2018", "bleh")
recipe_book.__check_values__()

def get_recipe_by_name(self, name):
    # Print a recipe with the name "name" and return the instance
    pass 

def get_recipe_by_type(self, recipe_type):
    """Get all recipe names for a given recipe_type """
    pass

def add_recipe(self, recipe):
    """Add a recipe to the book and update last_update"""
    pass