#Indentation is very important
print("FOR LOOP!!")
for i in range(1,13):
    print("No. {} square is {} cubed is {:4}".format(i,i**2,i**3))
    print("@"*40)#inside of for loop
print("*"*80) #outside of for loop

########################################################################
print("IF BLOCK!!")
name=input("Please enter your name: ")
age=int(input("How old are you?,{} ".format(name)))
print(age)
if age>=18 and age<=150:
    print("You are eligible to vote")
elif age>150:
    print("Damn! You're really young to vote")
else:
    print("Wait for another {} years to vote ;)".format(18-age))

#########################################################################

