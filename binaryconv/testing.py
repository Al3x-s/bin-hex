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
    
result = DecimalToBinary(255)
print(fixBinary(result))