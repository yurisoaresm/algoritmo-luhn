
# Identificar o tipo do cartão
def idCard (num):
    if str(num)[0] == '4':
        print('VISA')
    else:
        char = str(num)[0] + str(num)[1]
        if char == '34' or char == '37':
            print('AMEX')
        elif char == '51' or char == '52' or char == '53' or char == '54' or char == '55':
            print('MASTERCARD')


# Validar o número do cartão
def validateCard (num):
    checkSum = 0
    count = len(num) - 2
    while count > 0:
        str(num)[count]
        count -= 2


cardNum = int(input('Digite o número do cartão: '))

idCard(cardNum)