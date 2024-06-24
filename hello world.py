

"""
I am learning to code from scratch using the W3School online resources
This is with the intent of creating useful tools for the field of Linguistics
I am currently a PhD student in Diachronic Linguistics and use a lot of data crunching so this will help
"""
from random import betavariate


msg = "Hello world, Vulpes Nubes here" #this is a string
date = 23062024 #this is an int
print(msg, "today is the", date)
keywords = ["linguistics", "research", "coding"] #creating a small dataset
keyword1, keyword2, keyword3 = keywords #learning to unpack
print(keyword1)
print(keyword2)
print(keyword3)

#Now I'm going to set a few global variables and create a function
alpha = "Vulpin" #Expect a lot of fox references
theta = "Baby fox" #creates a global variable we will invoke and edit within a function

def invoker(): #and a lot of DND too
    alpha = "Fox"
    print(alpha) #this uses the above created variable, ignoring the global variable
    global beta
    beta = "Vixen"
    print(beta) #this prints a local variable that is set within the function on a glabally declared variable
    global theta
    print(theta) #print global variable before editing it
    theta = "Kit" #edit global variable
    
    
invoker() #this closes the function created and defined above
print(alpha) #this will display the global variable
print(beta) #this prints a global variable created within a function 
print(theta) #print global variable that was edited in the function