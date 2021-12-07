############ sorting ########################

from array import *
val=array('i',[7,8,3,4,1,9])
val=sorted(val)
print("ascending order : ", val)
val.reverse()
print("descending order : ", val)

######### reverse widout function ###########

print("\n")
a=array('i',[10,3,6,2,8,7,4,0])
b=a[::-1]
print('reversed array : ',b)
print("\n")

#### search and delete element at index 2 ####

b=array('i',[5,4,1,3,0])
print("Original array : ",b)
b=b[:2]+b[3:]
print("Index 2 element is deleted : " ,b)

