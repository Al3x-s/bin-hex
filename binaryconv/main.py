import random
import text
from tabulate import tabulate

#create an app to convert decimals to binary or convert binary to decimals

#create a random binary number with length 8

#create a random number 0-255
def Main():
    
    
    def createRandomBinary():
        randomBinary = ''
        for i in range(8):
            bit = random.randint(0,1)
            randomBinary += str(bit)
        return randomBinary
        #return String
        #DONE
        
    def createRandomDecimal():
        randomBinary = random.randint(0,255)
        return randomBinary
        #returns int
        #DONE
        
        
    #create function to make an 8 digit binary given the translate decimal function
    def fixBinary(givenNum):
        if len(givenNum) < 8: 
            difference = 8 - len(givenNum)
            for i in range(difference):
                givenNum = ''.join(('0',givenNum))
            return(givenNum)
        if len(givenNum) > 8:
            givenNum = givenNum[-8:]
            return(givenNum)
        #returns String
        #done

    #make sure to take a string in the argument
    def binaryToDecimal(binaryNum):
        x = 0
        #binaryNum = binaryNum[::-1]
        start = 7
        for i in range(len(binaryNum)):
            x += (2 ** start) * int(binaryNum[i])
            start -= 1
        return x
    
    
    def translateDecimal(decimal):
        binary = ''
        if decimal >= 1:
            binary = (decimal // 2)
        binary += str(decimal%2)
        return binary
        #fix variable names
        #returns String        
        #DONE
         
    ################################################################
    #try to create a try function
    def tryBinaryToDecimal(currentBinary, userInput, lives):
        correctAnswer = binaryToDecimal(currentBinary)
        if currentBinary == userInput:
            print("correct do you want to try again")
        else:
            print("not quite right")       
            lives -= 1
             
        

    
    ################################################################
    #try to create a try function
    #def tryDecimalToBinary()     

    
    
    ################################################################
    
    options = ['first', 'f', 'second', 's']
    
    tableRules = [["Do you want to convert binary to decimal?", "Enter 'first' or 'f'"], ["Or do you want to convert Decimal to Binary?", "Enter 'second' or 's'"]]
    
    information = [
        ["1", "You have 2 lives"],
        ["2", "Help is only available in the main menu"],
        ["3", "All decimal values are | 0 < x < 255"],
        ["4", "All binary values | 0 < x < 11111111"]
        ]

    formatted_table = tabulate(information, headers=["", "Information"], tablefmt="fancy_grid")
    items = [text.welcomeScreen[0],formatted_table]
    formatted_table = tabulate([items], tablefmt="fancy_grid")
    
    print(formatted_table)
    print(tabulate(tableRules))
    print("To exit press 'e'\n")
    
    ################################################################
    
    def playGame(startOption):
        lives = 2
        def printLives():
            print("lives " + str(lives))
        
        if startOption in ["first" ,'f']:
            newGameBinaryNum = createRandomBinary()
            printLives()
            print("the given binary = " + str(newGameBinaryNum))
            userAttempt = input("guess??")
            
        else:
            printLives()
            print("the given decimal = " + str(createRandomDecimal()))
            
        exit()
    
    while True:
        init = input("enter your choice    ")
        if init in options:
            playGame(init)
        if init == 'e':
            exit()
        else:
            print('not option please try again')
        
        
Main()  # Call the Main() function
