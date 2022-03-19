#and wil be true only when both the conditions are true
#or will be true even if one of the two conditions are true
#these conditions will work according to the truth tables of and & or
age=int(input("How old are you? "))
if age>=16 and age<=65:
    print("Have a good day at work!")
print("*"*60)
#same condition can be created in a simplified way
#different way of representing and
age=int(input("How old are you? "))
if 16<=age<=65:
    print("Have a good day at work!!")
else:
    print("Enjoy your free time :)")
print("*"*60)

#same program using or
age=int(input("How old are you? "))
if age<16 or age>65:
    print("Enjoy your free time :)")
else:
    print("Have a good day at work!!")
