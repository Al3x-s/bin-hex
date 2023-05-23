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
    
    def translateDecimal(decimal):
        binary = ''
        if decimal >= 1:
            binary = (decimal // 2)
        binary += str(decimal%2)
        return binary
        #returns String        
        #DONE
            
    
    options = ['first', 'f', 'second', 's']
    print(text.welcomeScreen[0])
    table = [["Do you want to convert binary to decimal?", "Enter 'first' or 'f'"], ["Or do you want to convert Decimal to Binary?", "Enter 'second' or 's'"]]
    print(tabulate(table))
    print("To exit press 'e'\n")
    
    def playGame(startOption):
        if startOption in ["first" ,'f']:
            print("the given binary = " + str(createRandomBinary()))
            
        else:
            print("the given decimal = " + str(createRandomDecimal()))
            
        exit()
    
    while True:
        init = input("enter your choice \n")
        if init in options:
            playGame(init)
        if init == 'e':
            exit()
        else:
            print('not option please try again')
        
        
Main()  # Call the Main() function
