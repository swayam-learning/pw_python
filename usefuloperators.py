from random import shuffle


for x in range(10):
    print(x)
for num in range(2,10):
    print(num)
for num in range(2,10,2):
    print(num)
index_count=0
word="abcde"
for letter in word:
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count +=1
index_count=0
word="abcde"
for letter in word:
    print(word[index_count]) #this is a list where string slicing is working
    index_count +=1
word="abcde"
for item in enumerate(word):  #gives tuples
    print(item)
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
mylist1 = [1,32,3,4,5,6,7]
mylist2=[2,4,56,78,69]  #they are going to ignore the extra items
for item in zip(mylist1,mylist2):
    print(item)
mylist1=[1,2,3,4,5,6]
mylist2=[4,5,6,7,8]
mylist3=['a','b','c','d','e']
for items in zip(mylist1,mylist2,mylist3):   #zip just joints everything
     print(items)
for a,b,c in zip(mylist1,mylist2,mylist3):
     print(a,b,c)
     print(b)
print(2 in mylist1)
print(min(mylist1))  #min is a function 
print(max(mylist1))  # max is also a function
from random import shuffle
mylist4=[53,67,45,35]
shuffle(mylist4) #shuffle is a function from random library
print(mylist4) #if we check the type of shuffle it is a none type
from random import randint
print(randint(0,100))


mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
print(mylist)
mynewlist=[x for x in 'word'] #this is list comprehension
print(mynewlist)
mynumberlist=[x for x in range(0,14)]   
print(mynumberlist)
mynumberlist=[x for x in range(0,14) if x%2==0]
print(mynumberlist)
mynumberlist=[x**2 for x in range(0,14)]
print(mynumberlist)
mynumberlist=[x**2 for x in range(0,14) if x%2==0]
print(mynumberlist) #all of these are types of list comprehension and we can use othe loops inside it
celsius=[20,56,89,45]
farhenheit=[((9/5)*temp+32) for temp in celsius]
print(farhenheit)
#list comprehension is just like appending something to a list
farhenheit=[]
results=[]
celsius=[20,56,89,45]
for temp in celsius:
   #we can also write in this way farhenheit.append(((9/5)*temp+32))
    farhenheit=(9/5)*temp+32
    results.append(farhenheit)
    print(farhenheit)
print(results)

