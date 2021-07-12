from sub_module import *
print('main',__name__)


print('main module welcome')



def fun1():
    sum2()
    print("from fun1")

def fun2():
    print("from fun2")

def main():
    fun1()
    fun2()

main()