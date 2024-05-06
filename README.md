name1= input("Enter his name: ")
name2= input("Enter her name: ")
name3= name1.lower()
name4= name2.lower()
name5= name3 + name4
print ( name5)
t= name5.count('t')
r= name5.count('r')
u= name5.count('u')
e= name5.count('e')
true= t+r+u+e
l= name5.count('l')
o= name5.count('o')
v= name5.count('v')
e= name5.count('e')
love= l+o+v+e
x= int(str (true) + str (love))
print ( x )
if(x>20 and  x<90):
    print (f"Nice jodi coz your love calculator range in {x}")
    if(x>40 and x<80):
        print (f"PURE LOVE IS THERE COZ LOVE CALCULATOR RANGE IN {x}")

else:
    print (f"Better luck next time")
