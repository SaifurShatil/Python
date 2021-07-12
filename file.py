f=open('mydata.txt','r')
print(f.readline())
print(f.readline())
print(f.readline(),end='') # end to remove extra line
print(f.readline(5),end='') # only print 5 char



f1=open('writefile.txt','w')
f1.write("something ")
f1=open('writefile.txt','a') #append
f1.write(" hp")


####copy

f=open('mydata.txt','r')
f1=open('writefile.txt','w')
#for data in f:
 #   print(data)

for data in f:
    f1.write(data)

############ files have char and binary format..
#image binary format

f2=open('shatil.jpg','rb') #read binary
#for i in f2:
#    print(i)

f3=open('mypic.jpg','wb') #write binary
for i in f2:
    f3.write(i)










