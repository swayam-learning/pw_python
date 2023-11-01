my_list = [1,'strings.45.67.','swayam']
my_anotherlist =[ 23,45,'swarup']
print(my_list + my_anotherlist)
my_list.append('dave')
print(my_list)
my_list.pop(3) #it removes the strings from the position specified
print(my_list)
my_list.pop()
print(my_list) #it pops the last element
new_list = ['a','j','e','b','c'] 
new_list.sort()#it sorts the element in order #if we try to store it another variable it doesnot return anything
my_sorted_list=new_list.sort()
print(my_sorted_list) 
#but if we assign to another varaible like this
my_sorted_list=new_list
print(my_sorted_list) 
print(new_list)
num_list=[1,2,3,45,67]
num_list.reverse()
print(num_list)
fruits=["apple","banana","cherry"]
points=(1,4,5,9)
fruits.extend(points)
print(fruits)
# lists are mutable.
# are heterogenous.
a=[["swayam","swarup"],["barik"]]
print(a[0][1])  # indexing a multidimensional list.
#append() is use elements to a list
#pop() is used to remove a character from a list.
# insert(position," string or number to be added")
# extend() is used to add elements this can only add elements to the end.
#.reverse() is used to reverse a list.
# .remove() is used to remove an elemnt from the list
# .pop() can only remove elements from the last of the list.
# list comprehension
odd_square = [x**2 for x in  range(1,11) if x%2==1]
print(odd_square)
# variable=[expression for element in old list if condition]
list=[1,2,3,4,5,6,7,5,5,7,8]
i=list.index(5)
list=list[:i]+["swayam"]+list[i+1:]
print(list)
for i in range(0,len(list)):
    if list[i]== 5:
        list[i]="swayam"

print(list)
# index() returns the index of the first matched item.
# copy() returns a copy of the list.
# sort() sort items in a list.
# max() returns the maximum element of a given list.
# min() returns the minnimum elemnt of a given list.
# all() returns true if all elements are true.
# ord() returns a unicode version of a given character.
# chr() returns a character for a numeric value.
# sum() sums up the function in the list.
# max() maximum element of a given list.
# min() minnimum element of a given list.
import functools
import operator
lis=[1,2,3,4,5,6]
print(functools.reduce(operator.add
,lis))
# here reduce function reduces the whole list to one value
list=["swayam","swarup","barik"]
print(functools.reduce(operator.add,list))
#reduce(func,seq) and is imported by functools.
#accumulate(seq,func) and 



