import random
from tabulate import tabulate

def Main():
    
    def createRandomBinary():
        random_binary = ''
        for _ in range(8):
            bit = random.randint(0, 1)
            random_binary += str(bit)
        return random_binary
    
    def createRandomDecimal():
        random_decimal = random.randint(0, 255)
        return random_decimal
    
    def fixBinary(given_num):
        if len(given_num) < 8: 
            difference = 8 - len(given_num)
            given_num = '0' * difference + given_num
        elif len(given_num) > 8:
            given_num = given_num[-8:]
        return given_num
    
    def binaryToDecimal(binary_num):
        translated_decimal = 0
        start = 7
        for i in range(len(binary_num)):
            translated_decimal += (2 ** start) * int(binary_num[i])
            start -= 1
        return translated_decimal
    
    def translateDecimal(decimal):
        translated_decimal = ''
        if decimal >= 1:
            translated_decimal = str(decimal // 2)
        translated_decimal += str(decimal % 2)
        return translated_decimal
    
    def tryBinaryToDecimal(current_binary, user_input, lives):
        correct_answer = binaryToDecimal(current_binary)
        if current_binary == user_input:
            print("Correct! Do you want to try again?")
        else:
            print("Not quite right.")
            lives -= 1
            print("Lives:", lives)
            print("Not a valid input.")
        return lives
    
    options = ['first', 'f', 'second', 's']
    
    table_rules = [["Do you want to convert binary to decimal?", "Enter 'first' or 'f'"],
                   ["Or do you want to convert Decimal to Binary?", "Enter 'second' or 's'"]]
    
    information = [
        ["1", "You have 2 lives"],
        ["2", "Help is only available in the main menu"],
        ["3", "All decimal values are | 0 < x < 255"],
        ["4", "All binary values are | 0 < x < 11111111"]
    ]

    formatted_table = tabulate(information, headers=["", "Information"], tablefmt="fancy_grid")
    items = [text.welcomeScreen[0], formatted_table]
    formatted_table = tabulate([items], tablefmt="fancy_grid")
    
    print(formatted_table)
    print(tabulate(table_rules))
    print("To exit, press 'e'\n")
    
    def playGame(start_option):
        lives = 2
        
        if start_option in ["first", "f"]:
            new_game_binary_num = createRandomBinary()
            print("The given binary number is:", new_game_binary_num)
            
            while True:
                user_attempt = input("Guess the decimal conversion (0-255): ")
                if user_attempt.isdigit() and 0 <= int(user_attempt) <= 255:
                    break
                else:
                    print("Not a valid input.")
            
            lives = tryBinaryToDecimal(new_game_binary_num, user_attempt, lives)
        
        else:
            print("Lives:", lives)
            print("The given decimal number is:", createRandomDecimal())
            
        return lives
    
    while True:
        init = input("Enter your choice: ")
        if init in options:
            lives = playGame(init)
            if lives <= 0:
                print("Game Over")
                break
       
# This version was broken with the final break statement use it to look at 
# code but do not use it to test game logic.