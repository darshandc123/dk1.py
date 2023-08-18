x=lambda x:x+5
print(x(1))

y=lambda x,y:x+y
print(y(2,5))

#map
m=(10,5,9,13,21,34)
l=list(map(lambda x:x+1,m))
print(l)

#filter
lst=[10,1,2,3,5]
z=list(filter(lambda x:x%2,lst))
print(z)

#reduce
from functools import reduce
lst1=[10,5,9,13,21,34]
a=reduce(lambda x,y:x+y,lst1)
print(a)
