class GotCharacter:
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    def __init__(self, first_name = None, is_alive = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    
    def __print_house_words__(self):
        print(self.house_words)
    
    def die(self):
        self.is_alive = False
    
    def __dict__(self):
        class_dict = {
            "First name": self.first_name,
            "Last name": self.family_name,
            "Is alive" : str(self.is_alive),
            "House words": self.house_words
        }

        return class_dict
