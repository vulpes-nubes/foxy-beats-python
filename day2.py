#day 2 of learning python, code starts bellow

words_of_the_day = "Good day, ", "this ", "is ", "day: "
number_of_day = 2
#unpacking the words
word1, word2, word3, word4 = words_of_the_day
print(word1 + word2 + word3 + word4, number_of_day) #print the extracted words
print(words_of_the_day, number_of_day) #print without extracting: this makes it ugly

# --- Now going to play with functions and global/function vairables

greeting = "Good-"
greeting2 = "day"
def greetings ():
    greeting2 = "afternoon"
    print(greeting + greeting2)
greetings()
print(greeting + greeting2)

#now going to create a whole load of variables to test their usages
rope = str("This is a string") #string
whole = int(42) #a whole number as an int
decimal = float(13.7) #a decimal number
complicated = complex(1j) #a comlex number
shopping = list(("apples", "pears", "cherries", "carrots")) #a list of strings
tupy = tuple(("apples", "pears", "cherries")) #a tuple, not sure when to use this yet
ranch = range(7) #a range? let's see what it's for
oxfcam = dict(name="tree", category="plant", defnum=13) #a dictionary style variable
group = set(("letuce", "leaks", "peppers")) # a set of data points, here strs
icegroupe = frozenset(("frozen letuce", "frozen leaks", "frozen peppers")) # a set of data points, here strs but frozen this time
oneorzero = bool(3) # a boolean or two
nomnom = bytes(5) #a byte or three
nomaray = bytearray(7) #an array of bytes
brain = memoryview(bytes(5)) #not sure but it looks at memory
#now let's print all of that and see what it looks like
print(rope)
print(whole)
print(decimal)
print(complicated)
print(shopping)
print(tupy)
print(ranch)
print(oxfcam)
print(group)
print(icegroupe)
print(oneorzero)
print(nomnom)
print(nomaray)
print(brain)
#well that's going to be a lot to remember though it's certainly cool to use them all.
