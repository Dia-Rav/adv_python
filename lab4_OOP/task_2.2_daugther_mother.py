
class mother():
    def __str__(self):
        return self.who_am_i()
    def who_am_i(self):
        return 'I am mother'
class daugther(mother):
    def who_am_i(self):
        return 'I am daugther'

M = mother()
D = daugther()
print (M)
print (D)


#output:
#I am mother
#I am daugther
