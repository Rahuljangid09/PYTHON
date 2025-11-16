# Logical Operators
x=20
y=10

print(x==20 and y<x)
print(x<y and y==10)
print(x!=20 or y>x)
print(x!=10 or y>x)
print(not x!=10 or y>x )
print(not x!=20 or y>x)

# Membership Operators
string1= "Hello"
print('H' in string1)

L=(10,20,30,40)
print(50 in L)

# Identity Operators
x=10
y=10
print(x is y, x==y)
print(x is not y , x!=y)

# Bitwise Operators
x=10
y=50
print(bin(x))
print(bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)