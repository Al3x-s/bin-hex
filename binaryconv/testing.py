# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end='')
   
def DecimalToBinary(num):
    binary = ''
    if num >= 1:
        binary = DecimalToBinary(num // 2)
    binary+=str(num%2)
    return binary
   


def fixBinary(givenNum):
    if len(givenNum) < 8: 
        difference = 8 - len(givenNum)
        for i in range(difference):
            givenNum = ''.join(('0',givenNum))
        return(givenNum)
    if len(givenNum) > 8:
        givenNum = givenNum[-8:]
        return(givenNum)


#make sure to take a string in the argument
def binaryToDecimal(binaryNum):
    x = 0
    #binaryNum = binaryNum[::-1]
    start = 7
    for i in range(len(binaryNum)):
        x += (2 ** start) * int(binaryNum[i])
        start -= 1
    return x
        
xx = binaryToDecimal('10110101')
print(xx)


num = 0
if num not in range(256):
    print("this doesnt work")
    
x = '123'
x = int(x)
print(x)
print(type(x))