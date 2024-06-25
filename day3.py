#today starts day 3 of learning python 
#Today it's booleans and the start of if, then, else
import random as rand
a = rand.randrange(0, 99)
b = rand.randrange(0, 99)
c = rand.randrange(0,9999, 3)
d = str(a)
e = str(c)
if a < b:
    print("Yes", a, "is smaller than", b)
else:
    print("Nope", a, "is not smaller than", b)
#apparently, functions can return booleans too
def testFunction():
    return True
print(testFunction)
if testFunction():
    print("True")
else:
    print("Nope")
#let's also try the isinstance function
print(isinstance(a,int))
print(isinstance(b,float))
#ha, it's time for maths !
print(a + b)
print(b - c)
print(c * a)
print(a / b)
print(b % c) #modulus
print(a ** b) #exponential
print(c // b) #floor division
#there are a whole load of other operators that I'm not going to test even if i'll probably use them in the future
print(a is b) #true if same number
print(a is not b) #true if they are not the same
print(d in e) #true if a is contained in c
print(d not in e) #true if b is not containted in c
#that's it for booleans and basic operators, now on to lists
myList = ["a word", 245, 25.452, "another word", 178.987, True]
print(len(myList))
print(myList[0], myList[-1])
print(myList[2:5])
print(myList[2:], myList[:3])
#now to test the list
if 178.987 in myList:
    print("Yes it has a 'True' in there")
else:
    print("Nope, that is not in there")
#now we edit the list
myList[3] = ["a new word"]
print(myList)
myList[0:2] = ["a different word", 1578, 68.98]
print(myList)
myList[4] = ["more words", 45787, False, True, True]
print(myList)
myList[2:3] = ["Hello there"]
print(len(myList))
print(myList)
myList.insert(0, "potato") #inserts a new word at that pos
print(myList)
