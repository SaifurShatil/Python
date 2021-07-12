#object, class, encapsulation, abstraction, polymorphism
#function-> method
#class - > design
#class have attributes (variables) & behaviour(methods)
#object -> instance

################################################
###class & object

class Computer:
    def config(self):
        print('i5 16gb 1tb')


com1= Computer()
com2=Computer()

print(type(com1))

Computer.config(com1)
com1.config()

Computer.config(com2)
com2.config()



