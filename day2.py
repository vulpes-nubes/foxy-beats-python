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
