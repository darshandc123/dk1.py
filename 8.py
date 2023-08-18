l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[1,1,1,1]
l=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print(l)

fruit=['mango','orange','apple','kiwi']
z=list(filter(lambda x: 'g' not in x ,fruit))
print(z)
