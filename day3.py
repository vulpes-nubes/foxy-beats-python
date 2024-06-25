#today starts day 3 of learning python 
#Today it's booleans and the start of if, then, else
import random as rand
a = rand.randrange(0, 99)
b = rand.randrange(0, 99)
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
