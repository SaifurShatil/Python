d={1:'jsh',2:'jhdhdf',4:'jfdhjr'}
print(d[4])
print(d.get(2))
print(d.get(3,'Not Found'))
print(d.get(1,'Not Found'))
print(d.keys())
print(d.values())

keys=[1,2,3,'y']
val=[34,'drtt',4.7,45]

data=dict(zip(keys,val))
print(data)

print(data['y'])
data['mon']=87
print(data)

del data[3]
print(data)

mul={1:43,2:[23,45],3:{1:34,4:9}}
print(mul)
print(mul[1])
print(mul[2])
print(mul[2][1])
print(mul[3][4])


