import random
import text
from tabulate import tabulate

#create an app to convert decimals to binary or convert binary to decimals

#create a random binary number with length 8

#create a random number 0-255
def Main():
    
    def createRandomBinary():
        random_binary = ''
        for i in range(8):
            bit = random.randint(0,1)
            random_binary += str(bit)
        return random_binary
        #return String
        #DONE
        
    def createRandomDecimal():
        random_decimal = random.randint(0,255)
        return random_decimal
        #returns int
        #DONE
        
    #create function to make an 8 digit binary given the translate decimal function
    def fixBinary(given_num):
        if len(given_num) < 8: 
            difference = 8 - len(given_num)
            for i in range(difference):
                given_num = ''.join(('0',given_num))
            return(given_num)
        if len(given_num) > 8:
            given_num = given_num[-8:]
            return(given_num)
        #returns String
        #done

    #make sure to take a string in the argument
    def binaryToDecimal(binary_num):
        translated_binary = 0
        #binaryNum = binaryNum[::-1]
        start = 7
        for i in range(len(binary_num)):
            translated_binary += (2 ** start) * int(binary_num[i])
            start -= 1
        return translated_binary
    
    
    def translateDecimal(decimal):
        translated_decimal = ''
        if decimal >= 1:
            translated_decimal = (decimal // 2)
        translated_decimal += str(decimal%2)
        return translated_decimal
        #fix variable names
        #returns String        
        #DONE
         
    ################################################################
    #try to create a try function
    def tryBinaryToDecimal(current_binary, user_input, lives):
        correct_answer = binaryToDecimal(current_binary)
        if current_binary == user_input:
            print("correct do you want to try again")
        else:
            print("not quite right")       
            lives -= 1
        return lives
             
        

    
    ################################################################
    #try to create a try function
    #def tryDecimalToBinary()     

    
    
    ################################################################
    
    options = ['first', 'f', 'second', 's']
    
    table_rules = [["Do you want to convert binary to decimal?", "Enter 'first' or 'f'"], ["Or do you want to convert Decimal to Binary?", "Enter 'second' or 's'"]]
    
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
    print(tabulate(table_rules))
    print("To exit press 'e'\n")
    
    ################################################################
    
    def playGame(start_option):
        lives = 2
        def printLives():
            print("lives " + str(lives))
        
        if start_option in ["first" ,'f']:
            new_game_binary_num = createRandomBinary()
            print("the given binary = " + str(new_game_binary_num))
            #user_attempt = input("guess??")
            # set a lives value == to the function that checks the user input the functions 
            #always returned the value but they were never saved
            while True:
                user_attempt = input("number within 0-255")
                if user_attempt.isdigit():
                    if 0<= int(user_attempt) <=255:
                        print("exception works")
                        break
                    else:
                        print("number out of range")
                else:
                    print("that isnt a number!")
            tryBinaryToDecimal(new_game_binary_num, user_attempt, lives)
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
