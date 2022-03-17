value="Norwegian Blue"
#upto the upper range not including it
print(value[0:6])
print(value[3:5])
print(value[3:7:3]+value[8:9])
print(value[0:]) #printing entire string
print(value[:])
print(value[:1])

#Negative Slicing
print("Negtaive Slicing")
print(value[-7:-3])
#Slicing moves in forward direction
print(value[-4:-1])


#using Steps in slicing
print(value[0:9:2])
print(value[0:9:3])
print(value[0::2])

#Negative steps in slicing
#for negative slicing start value must be greater than stop value
letter='abcdefghijklmnopqrstuvwxyz'
print(letter[25:0:-1])
print(letter[25:0:-2])
print(letter[25::-1]) #for including every value
#python slicing idiom for reverse
print(letter[::-1])

print(letter[16:13:-1])
print(letter[4::-1])
print(letter[25:17:-1])

print(letter[:-9:-1])

#Python idioms of slicing
print("Python idioms!!")
print(letter[-5:]) #printing last n characters
print(letter[-1:]) #printing last character
print(letter[:1]) #printing first character
print(letter[0]) #printing  character at given index



