# Square of a number
a=int(input("Enter the number for squaring:"))
s=a*a
print(s)
# Sum of number
b=int(input("Enter value of b :"))
c=int(input("Enter value of c :"))
d=b+c
print("Sum is {}".format(d))
#Swapping of 2 numbers 
f=int(input("Enter value of f :"))
v=int(input("Enter value of v :"))
h=f
f=v
v=h
print("Number after swapping is {}".format(f))
print("Number after swapping is {}".format(v))
# To check even or odd
x=int(input("Enter value of x :"))
if x%2==0 :
    print("The entered number is even ")
else :
    print("Entered no. is odd")
# Guessing game
j=6    
g=int(input("Enter value of g :"))
if g==j :
    print("You have guessed the number right")
else   :
    print("You have guessed the wrong number")
#Type of variables    
a=5
print(type(a))
l=5.7
print(type(l))
m="Heyy"
print(type(m))
a=1
b=False
c=22.785
d=23+3j
print(type(a) ,type(b) , type(c) ,type(d))
#Celsius to fahrenheit
t=int(input("Enter the temperatue in celsius : "))
f=(9/5*t)+32
print(f)
#Cube root of a number
p=int(input("Enter the number for cube root :"))
j= round(pow(p,(1/3)))
print(j)