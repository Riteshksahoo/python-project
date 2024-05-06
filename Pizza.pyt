print("WELCOME TO THE PIZZA SHOP \n" "HOW MAY I HELP YOU?\n")
SIZE= input ("PLEASE,PROVIDE US THE SIZE OF THE PIZZA \n" "PIZZA IS PRESENT IN THE SIZE OF THE (S\M\L) OR (s\m\l)\n")
price=0
if(SIZE== 'S' or SIZE=='s'):
    price=price+100
    print(f"The size of the PIZZA is {SIZE} and the price is {price}")
elif(SIZE=='M' or SIZE=='m'):
    price=price+200
    print(f"The size of the PIZZA is {SIZE} and the price is {price}")
elif(SIZE=='L' or SIZE=='l'):
    price=price+300
    print(f"The size of the PIZZA is {SIZE} and the price is {price}")
else:
    print("The size of the PIZZA you have entered is not present or unavailable.Sorry,please put correct Size")


ADD_ON= input ("WOULD YOU LIKE TO ADD ON IN THE PIZZA (Y/N) or (y/n)?")
if (ADD_ON=='Y' or ADD_ON=='y'):
    if(SIZE=='S'or SIZE=='s'):
     price=price+30
     print(f"The size of the PIZZA is {SIZE} and the price is {price} after Adding")
     if(SIZE=='M'or SIZE=='m'):
        price=price+30
        print(f"The size of the PIZZA is {SIZE} and  the price is {price} after Adding")
    elif(SIZE=='L' or SIZE=='l'):
       price=price+30
       print(f"The size of the PIZZA is {SIZE} and the price is {price} after Adding")
if (ADD_ON=='N' or ADD_ON=='n'):
    print(f"The size of the PIZZA is {SIZE} and the price is {price}")
