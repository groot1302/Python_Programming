string1="he's "
string2="probably "
string3="pining "
string4="for the "
string5="fjords"

print(string1+string2+string3+string4+string5)
print("Anshika "*5) #strings can be multiplied
#concatination can be done only within strings

#to check if a string is substring of other
today="friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("ansh" in "anshika")
print("fri" in "burger")
print("\n")

#String replacement fields for concatinations
print("STRING REPLACEMENTS!!")
age=25
print("My age is "+ str(age)+ " years")
#Formatting strings in much easier way
age=25
print("My age is {0} years".format(age))

#string formatting for multiple values of replacemnt fields
#replacement fields start from {0}
#{} represents the replacement fields
days=30
years=2020
print("There are {0} days in most of the months of year {1}".format(days,years))

#directly using values instead of variables

days=30
print("There are {0} days in most of the months of year {1}".format(days,"2020"))
print("There are {0} days in most of the months of year {1}".format(30,2020))
print("\n")

#STRING FORMATTING
print("STRING FORMATTING!!")
#the value after : determines the bit space it will take on output console
print("There are {0:3} days in most of the months of year {1}".format(days,"2020"))
print("My favourite number is {0:5}".format(100))

#Aligning the value to left side
print("My favourite number is {0:<5}".format(100))

#to center align the values
print("My favourite number is {0:^5}".format(100))

#it also helps in deciding the space for a float value
#it will take atleast 12 spaces and will show whitespace only if value is less than that
print("The value of pi is {0:12}".format(22/7))

#deciding the format for spacing not precision
print("The value is {0:6}".format(5/2))

#USING F STRINGS FOR TYPE CONVERSION
age=20
age2=100
print(f"My age is {age} years ;)")
print(f"My sister's age is {age2} years ;)")
print(f"Pie is approximately {22/7}")