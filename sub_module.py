

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


print('Hello ' + __name__)


def main():

    print('hello')
    print('welcome user')

if __name__=='__main__':
    main()
#####################################

def sum2():
    print('sum',__name__)
def sub2():
    print('sub')

def main1():
    sub2()
    sum2()
if __name__ == '__main__':
    main1()