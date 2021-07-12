from numpy import arange

from array import *
vals= array('i',[3,-4,56,7])
print(vals.buffer_info())
print(vals.typecode)
vals.reverse()
print(vals)
print(vals[0])

for i in range(len(vals)):
    print(vals[i])
print( )
for e in vals:
    print(e)

char=array('u',['a','e','i','o','u'])
for c in char:
    print(c)

#copy
newArr= array(vals.typecode, (a for a in vals))
for p in newArr:
    print(p)

newArr2=array(vals.typecode, (a*a for a in vals))
for j in newArr2:
    print(j)

i=0
while i<len(newArr2):
    print(newArr2[i])
    i+=1

# array value from user
from array import *
arr= array('i',[])
n = int(input('Enter length of array:'))
for i in range(n):
    x=int(input('Enter the nxt val:'))
    arr.append(x)
print(arr)

val=int(input('Enter the value to search:'))
k=0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

print(arr.index(val))

######## delete

ta=array('i',[45,64,22,67,9])
for i in range(len(ta)):
    if i==2:
        ta.pop(i)
print(ta)

#####reverse
ta=array('i',[45,64,22,67,9])
c=len(ta)
c=c-1
print(c)
newArr3=array('i',[])
while c>=0:
    newArr3.append(ta[c])
    c-=1
print(newArr3)


######numpy
from numpy import *
arr=array([2,3,4,5,6.0])
arr1=array([2,3,45,67], float)
print(arr)
print(arr.dtype)
print(arr1.dtype)
#####multi dimension(array, linspace, logspace,arange,zeros,ones)
from numpy import *
arr=array([2,3,4,5,6])
arr2=linspace(0,15,16)
print(arr2)
arr3=linspace(0,15,20)
print(arr3)
arr4=linspace(0,15)#default breaking part 50
print(arr4)

###arange
from numpy import *
arr5=arange(1,15,2)# skip 2 value
print(arr5)

#logspacef
from numpy import *
arr6=logspace(1,40,5) #log based values
print(arr6)
print('%.2f'%arr6[0])

##zeros,ones
from numpy import *
arr7= zeros(5)
print(arr7)
arr8=ones(5,int)
print(arr8)

###########  Array operation(addition, aliasing, shallow & deep copy)

from numpy import *
arr= array([1,2,3,4,5])
arr=arr+5
print(arr)

arr1=array([4,5,6,7,8])
arr3=arr+arr1
print(arr3)
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

from numpy import *
arr= array([1,2,3,4,5])
arr1=array([4,5,6,7,8])
print(concatenate([arr,arr1]))

#copy
from numpy import *
arr=array([1,2,3,4,5])
#aliasing(new alias of the same array-same address)
arr2=arr
print(arr)
print(arr2)
print(id(arr))
print(id(arr2))

#diff address
arr3=arr.view()
print(arr)
print(arr3)
print(id(arr))
print(id(arr3))

#shallow copy(both array r still dependent)
arr3=arr.view()
arr[1]=7  #arr3 will change also
print(arr)
print(arr3)
print(id(arr))
print(id(arr3))

#deep copy
from numpy import *
arr=array([1,2,3,4,5])
arr4=arr.copy()
arr[1]=7  #arr4 will not change
print(arr)
print(arr4)
print(id(arr))
print(id(arr4))

###### matrix multiplication- 2d

from numpy import *
arr=array([
    [1,2,3],
    [4,5,6]
])
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape) #rows cols
print(arr.size)

arr1=arr.flatten()#multi to single dimension
print(arr1)

#single to multi dimension
arr2=array([
    [1,2,3,7,8,3],
    [4,5,6,2,1,4]
])
arr3=arr2.flatten()#multi->single
arr4=arr3.reshape(3,4)# single-> multi (rows, cols) 2d
print (arr4)
arr5=arr3.reshape(2,2,3) #3d (2 2d array, 2 row(1d array), 3 col)
print(arr5)

#multiplication
arr2=array([
    [1,2,3,7],
    [4,5,6,2]
])

m=matrix(arr2) #array to matrix to perform more operations
m1=matrix('1,2,3,7;4,5,6,2')
print(m)
print(m1)

m2=matrix('1,2,3;7,4,5;6,2,9')
print(m2)
print(diagonal(m2))
print(m2.min())
print(m2.max())

m3=matrix('1,2,3;7,4,5;6,2,9')
m4=matrix('1,8,3;7,3,5;1,2,9')
m5=m3+m4
print(m5)

m6=m3*m4
print(m6)
























































