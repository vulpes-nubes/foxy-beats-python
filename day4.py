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
