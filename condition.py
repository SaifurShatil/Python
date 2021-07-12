#debug f8

x=int(input())
if x==1:
    print('one')
elif x==2:
    print('two')
else:
    print('wrong')



#while
i=1
while i<=5:
    print('hi')
    i+=1

######
j=1
while j<=5:
    print('hi',end="")
    j+=1
    k=1
    while k<=4:
        print('sha',end="") #same line er jonno end=""
        k+=1
    print() #newline

# For

x=[23,6.7,'naJ']
for i in x:
    print(i)
x='shatil'
for i in x:
    print(i)
for i in range(len(x)):
    print(x[i])
for i in {34,0,76,'gk'}:
    print(i)
for i in range(10):
    print(i)
for i in range(11,20,2):
    print(i)

for i in range(20,11,-1):
    print(i)

for i in range(10,21):
    if i%5!=0:
        print(i)


#####
av=6
i=1
x=int(input("how many:"))
while i<=x:
    i += 1
    if x>av:
        break
    print(i)

####
for i in range(50):
    if i%3==0 or i%5==0:
        continue
    print(i)
######
for i in range(50):
    if i%2==0:
        pass #no code
    else:
        print(i)


#####   for else
x=[45,9,25,67,87]
for i in x:
    if i%2==0:
        print(i)
        break
else:
      print('not found')


###
n=9
for i in range(2,n):
    if n%i==0:
        print('not prime')
        break
else:
    print('prime')






