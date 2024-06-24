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

#it's time to practice with number and changes
x = 7 #an int
y = 42.5 #a float
z = 3j #a complex
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#now going to play with randoms, it's time to build a d20
import random #bring in the library to create randos
print(random.randrange(1, 20)) #creates a D20

#time to play with new strings
dumb_quote = """Hello world is a beautiful thing
it creates a base for all to start from
now to see where it will bring
our beautiful project. To prom?""" #this makes a nice long quote
print(dumb_quote)

#so apparently, strings are arrays and thus i can play with that
print(dumb_quote[4]) #should give the fifth letter of the string

for letter in "platypus": #run through the string and print the letters
 print(letter)

print(len(dumb_quote)) #gives the string length 

print("beautiful" in dumb_quote) #looks for the word in the string and say if it's there
print("potato" not in dumb_quote) #looks if not in the string and print t/f

if "beautiful" in dumb_quote:
 print("Yes, 'beautiful' is in that quote") #same thing with an if clause

if "potato" not in dumb_quote:
 print("correct, there is no potato in there")

#now it's time to slice this up
print(dumb_quote[12:16]) #prints position 13 to 17 in the string
print(dumb_quote[:5]) #prints from start to position 6 in the string
print(dumb_quote[118:]) #prints from position 121 to end of string
print(dumb_quote[-17:-10]) #starts the print from the back of the string

#let's edit those strings
print(dumb_quote.upper()) #print the string made fully caped
print(dumb_quote.lower()) #print the string as lowercase only
print(dumb_quote.strip()) #print the string with no spaces before or after (there were none anyway heck)
print(dumb_quote.replace("o", "e"))
print(dumb_quote.split("thing")) #splits the string at 'thing'

#now we need new strings to play with
waou = "flying"
heck = "potato"
seriously = waou + heck #add the two together into a new string
print(seriously)
space_seriously = waou + " " + heck #add a space in there
print(space_seriously)

#now let's make an f-string to not be confused with a fing string

