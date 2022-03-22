#until the condition is true loop keeps on working
#as soon as condition becomes false loop terminates
#used in cases when we can't actually predetermine the number of times a loop has to work

#initialize 2)give condition 3)print 4)increment the value

#this given example both loops will give the same value
for i in range(10):
    print("i is now {}".format(i))

i=0
while(i<10):
    print("i is now {}".format(i))
    i+=1
print("*"*60)

#infinite loop
#while True:
   # print("i is now {}".format(i))


available_exits=["north","south","east","west"]
chosen_exits=""
while chosen_exits not in available_exits:
    chosen_exits=input("Please choose a direction: ")

print("We are out of the place")
print("*"*60)

print("Break in while loop")
available_exits=["north","south","east","west"]
chosen_exits=""
while chosen_exits not in available_exits:
    chosen_exits=input("Please choose a direction: ")
    #another way for same if condition
    #if chosen_exits=="quit":
    if chosen_exits.casefold()=="quit":
        print("GAME OVER!")
        break

print("We are out of the place")