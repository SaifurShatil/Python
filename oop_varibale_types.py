# 2 types
# instance variable -> changes for each obj -> inside init
# class(static variable) -> outside init

class Car():
    wheel=4
    def __init__(self):
        self.mil=10  #
        self.com='bmw' # instance var


c1=Car()
c2=Car()
c1.mil=8

print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)

Car.wheel=5
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)















