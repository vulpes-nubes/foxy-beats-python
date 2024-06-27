#here starts day 4 of learning python coding
myList = ["a word", 245, 25.452, "another word", 178.987, True] #copy from day three to have a list to work with
myList.append(1234)
print(myList)
newTuple = ("Hello", "World", 2345)
myList.extend(newTuple) #extends one list with any other iterable
print(myList)
myList.remove("another word") #removes first occurence of the item
print(myList)
myList.pop(3) #removes specific position in the list
print(myList)
sorryList = ["A List to be deleted", 1234, 45643, "potato"]
del sorryList #deletes the entire list
sorryList2 = ["Another sorry list", 352345, 1435, True]
sorryList2.clear()
print(sorryList2)
for x in myList: #runs through list items
    print(x)
for i in range(len(myList)): #runs through content of list indexes 
    print(myList[i])
j = 0
while j < len(myList):
    print(myList[j])
    j = j + 1

[print(x) for x in myList]