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
    def __str__(self):
        text = ' '.join(['Name:', self.get_name(), '\n',
                       'Age:', str(self.get_age()), '\n',
                       'Type of animal:', self.get_type(), '\n'])
        return text
class zebra (animals):
    _type = 'Ungulates'

class dolphin (animals):
    _type = 'Delphinidae'

Z = zebra('Marti', 18)
D = dolphin('Eva', 5)
print (Z)
print (D)