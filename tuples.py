t=(2,'swayam',69,57)
print(type(t)) #tuples are immutable
print(t.count(2)) #it counts the number of time 2 appears in the tuple
print(t.index(2))  #it tells the first time 2 appears in the tuple
# len() used to calculate lenght of a tuple,
# max() , min() , sorted() is also used in tuples.
# all() returns true if all elements are true 
# any() returns true if any elemnt of a tuple is true.
# enumerate(iterable,start value(usually 0)) enumerates the string.
# sorted() function can be used with any data type with strings it sorts according to the ASCII translations.
tuple=("swayam","swarup","barik")
for e in enumerate(tuple,100):
    print(e)
# sorted(iterable,key,reverse)  key and reverse are optional
#if reverse is set true than it returns the sorted() in descending order.
# tuple are immutable and faster than list.
tuple1=(12,34,56,78)
print(tuple1[::-1])
x=(sorted(tuple1,reverse=True))
print(x)
tuplke1=(1,2,3,3,4,5,6,7,7)
print(tuplke1)