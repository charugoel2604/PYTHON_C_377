a = 40
b = 20
c = a & b;
print ("result of AND is ", c,':', ':',bin(c))
c=a|b;
print ("result of OR is ", c,':',bin(c))
c=a^ b;
print ("result of EXOR is ", c,':',bin(c))
c = ~a;
print ("result of COMPLEMENT is ", c,':',bin(c))
c = a << 2;
print ("result of LEFT SHIFT is ", c,':',bin(c))
c = a >> 2;
print ("result of RIGHT SHIFT is ", c,':',bin(c))

var = 8
print(var > 2 and var < 10)
print(var > 2 or var < 4)
print(not (var > 2 and var < 10))

a = [1,2,3,5]
b = [1,2,3,5]
c = b
print(a is c)
print(a is b)
print(a is not c)
print(a is not b)