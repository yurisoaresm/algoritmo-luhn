
# Identificar o tipo do cartão
def idCard (num):
    if str(num)[0] == '4':
        print('VISA')
    else:
        if str(num)[0:2] in ['34', '37']:
            print('AMEX')
        elif str(num)[0:2] in ['51', '52', '53', '54', '55']:
            print('MASTERCARD')


# Validar o número do cartão
def validateCard (num):
    checkSum = 0
    listNum = []
    count = len(num) - 2
    while count > 0:
        str(num)[count]
        count -= 2


cardNum = int(input('Digite o número do cartão: '))

idCard(cardNum)