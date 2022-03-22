shopping_list=["egg","rice","chocolates","toffees","curd","riceballs"]
for items in shopping_list:
    if items!="egg":
        print("buy"+ items)

for items in shopping_list:
    #continue will run the loop but without the mentioned statement
    #mentioned condition value will be skipped
    #next associated statement has to be with the same indentation as if
    if items=="egg":
        continue
    print("buy"+ items)
print("*"*60)

print("BREAK STATEMENT!!")
shopping_list=["egg","rice","chocolates","toffees","curd","riceballs"]
#break statement will terminate the loop as soon as the condition is encountered
for items in shopping_list:
    #next associated statement has to be with the same indentation as if
    #used to jump out of a loop when condition is satisfied
    if items=="egg":
        break
    print("buy"+ items)
print("*"*60)


#Another program of break
shopping_list=["egg","rice","chocolates","toffees","curd","riceballs"]
item_to_find="toffees"
#value is initialized to none(doesn't have any value)
#if not initialized it will give an error
found_at=None
for index in range(len(shopping_list)):
     if shopping_list[index]==item_to_find:
         found_at=index
         #break is used to terminate the loop when condition is satisfied
         break
if found_at is not None:
    print("Item found at position {0}".format(found_at))
else:
    print("Item not found".format(item_to_find))