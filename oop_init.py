
# special method(__init__)
# to initialize variables
# called automatically when obj created

class Computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu  # assign values to an obj
        self.ram=ram

    def config(self):
        print('config is: ',self.cpu,self.ram)  # as cpu/ram is not a local variable (belongs to an object)

com1=Computer('i5', 16)
com2= Computer('Ryzen3', 8)

com1.config()
com2.config()














