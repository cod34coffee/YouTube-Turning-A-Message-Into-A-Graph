import numpy as np
import matplotlib.pyplot as plt

def chooseYesOrNo():
    #The encryptDecrypt is going to store your message.
    #The input() part, is what will allow you to type in a message to be stored.
    #The .lower() part, will make your answer lowercase whether you type in it lowercase or not. 
    encryptDecrypt = input("Do you want to encrypt your message? Type yes or no. ").lower()

    #Remember to indent when needed in python.
    #This is an if, with the elif included, and the else statement too, statment where I will test to see if the answer is "yes."
    #If the answer is "yes" the following will happen.
    if encryptDecrypt == "yes":

        #If the answer is yes, if will print "Time to encrypt."
        print("Time to encrypt.")
        wordsToEncrypt = input("What would you like to encrypt? ")

        #This below starts the count at zero.
        letterNumCount = 0

        #This will allow you to store stuff in it later.
        letterNum = []

        #This is going to perform until the "letterNumCount" becomes greater than the length
        #of "wordsToEncrypt"
        while letterNumCount < len(wordsToEncrypt):

            #For every item that passes through as "i", the following will happen.
            for i in wordsToEncrypt:
                #This below will turn the letters that get passed through into numbers.
                changeLetters = ord(i)

                #So now each of the numbers that were just created by turning the letters
                #from the message into numbers have been stored into the variable "changeLetters"
                #Since it is stored there now it is being attached and stored into the letterNum
                #from earlier.
                letterNum.append(changeLetters)

                #This below is keeping count of how many times the "while loop" happens. Once
                #it becomes greater than or equal to the length of wordsToEncrypt. No longer less
                #than wordsToEncrypt. The "while loop" will stop.
                letterNumCount += 1

        #After all of that, then it will reverse the order of everything.
        letterNum.reverse()

        #Now the "letterNum" is being stored in the y_axis.
        y_axis = letterNum
        #This below is going to print out what is stored in the y_axis.
        print(y_axis)


        x=range(1, len(y_axis) +1)
        y=y_axis

        plt.fill_between(x,y)
        plt.show()

        #Let's see if it displays. Okay that worked, but what if they type no?


    elif encryptDecrypt == "no":
        print("Well, I will catch you next time.")

    else:
        print("Sorry, I need you to type yes or no. ")

chooseYesOrNo()
#Let's test it out so far. So far so good. Now let's make this turn the message into a graph.
#Let's try it.
#Let's try a different message.
#That's it for today. 



        
       
