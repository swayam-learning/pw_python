print("range(10)-->",list(range(10))) #it always includes from o to 9
print("range(0,20)-->",list(range(0,20)))
print("range(10,20)-->",list(range(10,20)))
print("range(0,20,2)-->",list(range(0,20,2)))
print("range(10)-->",list(range(-10,20,2)))
print("range(-10,-20,2)-->",list(range(-10,-20,2)))   #the range is all negative but the steps are positive hence it will not show any result
print("range(-10,-20,-2)-->",list(range(-10,-20,-2)))