# List is ordered and changeable
list1=["Apang",5,3.3,"Apang","Apple","Apple"]
print(list1)
# list length
list1=["Apang",5,3.3,"Apang","Apple","Apple"]
print(len(list1))
#list() constructor
list2=list(("Apang",5,3.3,"Apang","Apple","Apple"))
print(list2)
# access item in list
list1=["Apang",5,3.3,"Apang","Apple","Apple"]
print(list1)
# copy list data to other list
list1=["Apang",5,3.3,"Apang","Apple","Apple"]
x=list1.copy
x=list(list1)
x=list1[:]
print(x)
# joint lists
s=['a','b','c']
v=['x','f','k']
z=s+v
print(z)
for x in v :
    s.append(x)
print(s)
s.extend(v)
print(s)