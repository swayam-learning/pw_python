A= 'abcdefghijk'
print(A)
b=A.strip()
print(b.rstrip('k'))
print(b.lstrip('a'))
A.rstrip('a').lstrip('k')
print(A)
print(A.count(b))
print(A.count(b,3)) # here 3 is the index location from where the strings starts counting
print(A[2])
print(A[-2])   #when we use negative it starts from -1 from the last
print(A[2:])   #this  one is slicing
print (A[-2:])
print(A[3:-7])  #this one is also slicing #position 7 is not included
print(A[::])   #this prints the whole string
print(A[::3])   #this prints everything from o position to 3rd position
print(A[2:3:2]) #this starts from 2nd position to 3rd postion and in step size of 2
print (A[::-1]) #this reverses the string
print(A.upper())
print(A.lower())
print(A.split()) #this will split string based on white spaces
print(A.split('b')) #this will only split the string where b is present
print('this is a string{}'.format(' INSERTED'))
print('the {} {} {}'.format('fox','brown','quick')) #the order of adding fox brown and quick was not we wanted
print('the{2} {1} {0}'.format('fox','brown',' quick')) #here the number represents the arrays position
#we can repeat the word by repeating their array  number
print('the {f} {b} {q}'.format(f='fox',b='brown',q='quick' ))
#another way of printing the statement using format
result=100/777
print("the result was {r:1.6f}".format( r=result)) #if we just write result it will show key error because it can't access the variable 
#{value:width.precision f} #width just adds blank space
 #another way of formatting a string is using 
name = 'jose'
print(f' hello,his name is {name}')
#or 
print('his name is {}'.format(name))
name="swayam"
age=3
print(f'his name is {name} and  his {age} yrs old')
print("swayam swarup barik")
# string is immutable.
# \t is used to give one tab space.
# \b is used as backspace.
# \ooo is used as octal form where the o is different numbers
# \xhh is used hexal form where h is two different numbers.
# \n is used to give new line.
# \r is used to move to next line.
# if we want write some text within quotes within already present string then we can use \"some text\"
# \' insert apostrophe  
# \\ this will insert ones string.
# .upper() writes the string in uppercase.
# .lower() writes the string in lowercase.
# .split() splits the string based on some mark.
# .strip() strip the string of white spaces.
# .rstrip() strip the string from right side 
# .lstrip() strips the string  from left side.
# .isupper() returns True if all the letters are in upper case.
# .isalpha() returns True if all characters in the string are alphabets.
# .isnumeric() returns True if all charcters in string are numbers.
# .isdigit() returns True if if all characters in strings are digits.
# .isdecimal() if all characters in the strings are decimals.
# .islower() if all the characters in the strings are in lower case.
# .isalnum() if all the characters in the strings are alphanumeric.
# .replace("value","value1") 
# .startswith("value") retrns True if the srings starts with the specified value.
# .swapcase() lowercase becomes uppercase and vice versa.
# .title() converts the first character of each word to upper case.
# we can use reversed() in python to  reverse a string.
# the syntax for that will be a="".join(reversed(x)) x will be some variable storing a string.
# only integers are allowed to be used as a string not float.

x="".join(reversed("swayam")) 
print(x)
print("i am \"strong\" ") # this is to print strong within double quotes.
# to ignore escape sequence r or R is used to represent this is a raw string.
# .partition() splits the string at the first occurence of the separstor and retruns as a tuple
print("geeks".partition("k"))
# the difference between the two is that the partition operator returns the separator but the split operator does not return the separator.
print("geeks".split("k"))
print("swayam , is , a , champion".replace(",",""))
A="this is a tutorial"
print(A.count("is",0,len(A)))    # count("substring",start,end)
str1="swayamswarupbarik"
print(str1.center(30,"-"))
print(str1.ljust(20,"-"))
print(str1.rjust(20,"-"))
# join() used to join the elemnts of the lists.
# find() and rfind() are used to find the first occurence of a substring and last occurence of a substring respectively and if the substring is not found it returns -1 as answer 
# syntax of find() and rfind() is similar to count().
  