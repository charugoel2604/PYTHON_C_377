list = ['hello', 377, 4.85, 'python']
list2 = [123,'python']
print (list)
print (list[0])
print (list[1:4])
print (list[3:])
print (list2*3)
print (list+list2)

for i in range(5):
    print(i)
for i in range(2,5):
    print(i)
for i in range(1,5,2):
    print(i)

set_a = {123,456,7,8,9}
set_b = {'Python','Java','Jupyter'}
list = {'number':3771 , 'language':'python'}
print(set_a)
print(set_b)
print(list.keys())
print(list.values())

x=None
print("x= ",x)
print("type of x = ",type(x))