def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i    
    print(fact)
    
factorial(int(input("")))  # here we are calling the function
def question(x,y):
    mult=x**y
    print(mult)

x=int(input("enter your 1st number:"))
y=int(input("enter your second number:"))
question(x,y)
#anything inside the paranthesis is called a parameter
#for multiple parameters we can use *infront he name of the parameter

def func(*a):
    print(a)

func(2,3,4,5,"swayam")
greater=lambda x,y: x if x>y else y
print(greater(2,3))