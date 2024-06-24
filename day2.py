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

anumber = 42 #create int
asentence = f"There are {anumber} flying potatoes here?!" #create str with a place holder for the int
print(asentence)
anothersentence = f"There are {anumber:.5f} flying coffee grinders too!" #add decimal points to be displayed
print(anothersentence)

#now to add a few fun modifiers
text = "This is going to be a \"test\" to see if I can get all \n of the magical things to \t work \t or \n not?"
# \" allows to use quotes inside others, \n makes a new line, \t adds a tabulation
print(text)

#now, I might not do all of the string methods, though there are certainly a lot... So i copy pasted the lot of them and will use them
testtext = """  this IS going to be a test text that I can use for all of the various str reading methods
 I hope that it will look and work properly.
 Let's now see {} if i did a good job or not.
 I do need a    tab."""
q = "vHts" #creates q, r, s as strings
r = "iaeo"
s = "lmn"
print(testtext.capitalize()) #Converts the first character to upper case
print(testtext.casefold())	#Converts string into lower case
print(testtext.center(25))	#Returns a centered string
print(testtext.count("I"))	#Returns the number of times a specified value occurs in a string
print(testtext.encode())	#Returns an encoded version of the string
print(testtext.endswith("."))	#Returns true if the string ends with the specified value
print(testtext.expandtabs(3))	#Sets the tab size of the string
print(testtext.find("look"))	#Searches the string for a specified value and returns the position of where it was found
print(testtext.format(42))	#Formats specified values in a string
#print(testtext.format_map())	#Formats specified values in a string don't know how it works
print(testtext.index("did"))	#Searches the string for a specified value and returns the position of where it was found
print(testtext.isalnum())	#Returns True if all characters in the string are alphanumeric
print(testtext.isalpha())	#Returns True if all characters in the string are in the alphabet
print(testtext.isascii())	#Returns True if all characters in the string are ascii characters
print(testtext.isdecimal())	#Returns True if all characters in the string are decimals
print(testtext.isdigit())	#Returns True if all characters in the string are digits
print(testtext.isidentifier())	#Returns True if the string is an identifier
print(testtext.islower())	#Returns True if all characters in the string are lower case
print(testtext.isnumeric())	#Returns True if all characters in the string are numeric
print(testtext.isprintable())	#Returns True if all characters in the string are printable
print(testtext.isspace())	#Returns True if all characters in the string are whitespaces
print(testtext.istitle()) 	#Returns True if the string follows the rules of a title
print(testtext.isupper())	#Returns True if all characters in the string are upper case
ineedatuple = ("Paul", "Atreidies", "Mu'hadib")
iwantaseperator = " - "
print(iwantaseperator.join(ineedatuple)) #Joins the elements of an iterable to the end of the string
print(testtext.ljust(2))	#Returns a left justified version of the string
print(testtext.lower())	#Converts a string into lower case
print(testtext.lstrip())	#Returns a left trim version of the string
print(testtext.maketrans(q, r, s))	#Returns a translation table to be used in translations
print(testtext.partition("if"))	#Returns a tuple where the string is parted into three parts
print(testtext.replace("e", "a"))	#Returns a string where a specified value is replaced with a specified value
print(testtext.rfind("o"))	#Searches the string for a specified value and returns the last position of where it was found
print(testtext.rindex("a"))	#Searches the string for a specified value and returns the last position of where it was found
print(testtext.rjust(5))	#Returns a right justified version of the string
print(testtext.rpartition("if"))	#Returns a tuple where the string is parted into three parts
print(testtext.rsplit("look"))	#Splits the string at the specified separator, and returns a list
print(testtext.rstrip())	#Returns a right trim version of the string
print(testtext.split("all"))	#Splits the string at the specified separator, and returns a list
print(testtext.splitlines())	#Splits the string at line breaks and returns a list
print(testtext.startswith("hello"))	#Returns true if the string starts with the specified value
print(testtext.strip())	#Returns a trimmed version of the string
print(testtext.swapcase())	#Swaps cases, lower case becomes upper case and vice versa
print(testtext.title())	#Converts the first character of each word to upper case
ineedadict = {47: 58}
print(testtext.translate(ineedadict))	#Returns a translated string using a quick changer as created above
iwantatable = str.maketrans(q, r, s) #makes a translation table with the values from q, r, and s
print(testtext.translate(iwantatable)) #returns a translated version using the table created
print(testtext.upper())	#Converts a string into upper case
print(testtext.zfill(5))	#Fills the string with a specified number of 0 values at the beginning
