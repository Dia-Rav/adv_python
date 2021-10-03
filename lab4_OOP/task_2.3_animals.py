class animals:
    def __init__(self, name, age):
        self._age = age
        self._name = name
        return 
    
    def get_name (self):
        return self._name

    def get_age (self):
        return self._age

    def get_type(self):
        return self._type

    def get_str (self):
        text = ' '.join(['Name:', self.get_name(), '\n',
                       'Age:', str(self.get_age()), '\n',
                       'Type of animal:', self.get_type(), '\n'])
        return text
    def __str__(self):
        return self.get_str()

class zebra (animals):
    _type = 'Ungulates'
    __number_of_legs = 4
    
    def __init__(self, name, age, number_of_legs):
        super().__init__(name, age)
        self.__number_of_legs = number_of_legs
        
    def get_legs(self):
        return self.__number_of_legs
    
    def get_str(self):
        text = ' '.join(['Name:', self.get_name(), '\n',
                       'Age:', str(self.get_age()), '\n',
                       'Type of animal:', self.get_type(), '\n'
                       'N of legs:', str(self.get_legs())])
        return text

class dolphin (animals):
    _type = 'Delphinidae'

Z = zebra('Marti', 18, 4)
D = dolphin('Eva', 5)
print (Z)
print (D)

#Name: Marti
# Age: 18
# Type of animal: Ungulates
#N of legs: 4
#Name: Eva
# Age: 5
# Type of animal: Delphinidae
