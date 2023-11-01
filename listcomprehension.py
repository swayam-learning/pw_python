l1=["automobiles","swayam","swarup","barik"]
l2=[len(i) for i in l1]
print(l2)
l1=[1,2,4,5,6,6,7]
i=0
l2=[i**2 for i in l1]
print (l2)
for i,j in zip(l1,l2):
  print(i,"-",j)
#another way of printing square of each element of lists:
l1=[1,2,3,4,5,6]
l3=[]
for i in l1:
  l3.append(i**2)
print(l3)
list_1=["wood", "old", "apple", "big","item", "euphoria"]
l2=[i for i in list_1 if i[0] in "aeiou"]
print(l2)
l1=[1,2,3,4]
l2=[i**2 for i in l1]
print(l2)