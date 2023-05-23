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
   
result = DecimalToBinary(24)
print(type(result))
