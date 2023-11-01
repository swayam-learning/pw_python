#a==b  equaloperator
#a!=b  not equal to
#a>b   greater than
#a<b   less than
#a>=b  greater than equal to
#a<=b  less than equal to
#a+= 1 means a=a+1
#a-=1  means a=a-1
print('b'=='b' and 2==2)
print(1==1 or 2==2)
print(1<2>3)
print(1==1)
print(not(1==1)) # not is used to give the opposite answer of the expected answer
#any number is True  except 0 ,any string is true except empty strings ,any list,tuple,dictionaries are True except empty ones.
#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
# if we use isintance() function it checks if the particualr varible is of this particluar data type and then returns in boolean.
# & and operator
# | or operator
# ~ not operator
# // floor division 
# / division
# ** power
# % returns remainder
# = is an assignment operator but == is comparison operator.
# / and * have same precedence and hence follows Left to right associativity
# + and - have same precedence and hence follows left to right associativity
# ** and ** follows right to left associativity
# ternary opeartor a if a < b else b similar to this we can use diiferent conditions.
print(2**3**2)
print("geeks"*4)
any([True,False,False,True]) # it is similar to or operator if any one is true it returns true else false for empty and all false conditions
all([False,False,True,True]) # iot is similar to and operator if any one is false it returns false or else true for all true.
import operator
a=10
b=20
print(operator.add(a,b))
print(operator.sub(a,b))
print(operator.mul(a,b))
print(operator.truediv(a,b))
print(operator.floordiv(a,b))
print(operator.le(a,b))
print(operator.lt(a,b))
print(operator.ne(a,b))
print(operator.eq(a,b))
print(operator.ge(a,b))
print(operator.gt(a,b))

