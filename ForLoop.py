parrot="Norwegian Blue"
for character in parrot:
    print(character)
print("*"*60)

#Extracting values from user input
number=input("Please enter a series of number using separators you like")
separators=""
for char in number:
    #char here is not a variable it's used for accessing thE individual characters of the given string
    #char here is a keyword
    if not char.isnumeric():
        separators=separators+char
print(separators)
print("*"*60)


#Iterating range
#last value is not included
print("ITERATING RANGE!!")
for i in range(1,20):
    print("i is now {}".format(i))
print("*"*60)

for i in range(10):
    print("i is now {}".format(i))
print("*"*60)

for i in range(0,10,2):
    print("i is now {}".format(i))
print("*"*60)

for i in range(10,0,-2):
    #when moving from a larger to lower value we have to take negative steps
    print("i is now {}".format(i))
print("*"*60)

#to check if the given value is in the range
age=70
if age in range(20,31):
    print("Yes value is present")
else:
    print("Not present in the given range")
print("*"*60)

#Nested for loops
print("Nested for loops!!")
for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} and {2}".format(j,i,i*j))
    print("------------") #this will work according to the outer for loop

