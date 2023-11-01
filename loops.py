
loc="game'"
if loc=="auto shop":
  print("cars are cool")
elif loc=="bank":
  print("money is cool")
elif loc=="store":
   print("welcome to the store")
else:
    print("i do not know much")
    
mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
  if num%2==0:
    print ("number is even",num)
list_sum=0
for num in mylist:
   list_sum=list_sum+num

print(list_sum)
mo_list="hello world"
for H in mo_list:
  print(H)
mynew_list =(1,23,4,56,69)
for num in mynew_list:
  print(num)
mynews_list=[(1,2),(23,34),(46,56),(6,7)]
for num in mynews_list:
  print(num)
for a,b in mynews_list:
  print(a)  #this is tuple unpacking we can print only a that is the 
  print(b)   #first element or b that is the second element of each tuple 
  #or both a and b of the tuples
d={'key1':1,'key2':2,'key3':3}
for num in d:
  print(num)
for num in d.items():
  print(num)
for a,b in d.items():
  print (b)
for a,b in d.items():  #a = key, b= value
  print(a)
for num in d.values():
  print(a)   #why? only key 3 if a and only 3 if b
# dictionaries are very unordered so it won't return value in order
num=0
addsum=0
while num<5:
  addsum=addsum+num
  num=num+1
print("the sum is =", addsum)
if num<5:
  addsum=addsum+num
  num += 1
print("the sum is =",addsum)
#break breaks out of the current closest enclosing loop.
#continue goes to the top of the current enclosing loop
#pass does nothing at all
#while loop is used when we are not aware of the number of iterations.
#for loop is used when we are aware of the number of iterations.
l1=[1,2,3,4,5,6]
l3=[]
for i in l1:
  l3.append(i**2)
print(l3)




