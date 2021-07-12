
class computer():
    def __init__(self):
        self.name ='shatil'
        self.age =24
    def update(self): # self is directing to an object
        self.age= 25
    def compare(self ,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 =computer()
c2 =computer()
print(c1.name)
print(c2.name)
c2.name='rabbi'
c1.update()
print(c1.age)
print(c2.age)

if c1.compare(c2):
    print('they ARE same')
else:
    print('different')
