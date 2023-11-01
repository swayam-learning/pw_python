x= [str(x) for x in  input("Enter your numnber: ").split(",")]
print(x)
a=12
b=5
c=22
print(a,b,c,sep="-")  # here sep(),end(),flush() are keyword arguments whereas a,b,c are postional argument ,a positional argument can never follow keyword argument.
print(a,end="@")
print(b,c)
print(a)
print(b,c)
l=[1,2,3,4]
print(l)
print(*l) # this is a better way to print list