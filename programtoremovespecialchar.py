import string


i=0
s=list(input())
while i < len(s):
    if (ord(s[i])<ord("A") or ord(s[i])>ord("Z") and ord(s[i])<ord("a") or ord(s[i])>ord("z")):
        del(s[i])
        i-=1
    i+=1

x=str(s)
print(x)
def removeSpecialCharacter(s):
    t = ""
    for i in s:
        if(ord(i) in range(97,123) or ord(i) in range(65,91)):
            t+=i
    print(t)
s = "$Gee*k;s..fo, r'Ge^eks?"
removeSpecialCharacter(s)