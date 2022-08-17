
# Identificar o tipo do cartão
def id_card(num):
    if str(num)[0] == '4':
        print('VISA\n')
    else:
        if str(num)[0:2] in ['34', '37']:
            print('AMEX\n')
        elif str(num)[0:2] in ['51', '52', '53', '54', '55']:
            print('MASTERCARD\n')


# Validar o número do cartão
def validate_card(num):
    num = str(num)   # Conversão do número para String
    pair_sum = 0     # Armazena os dígitos começando pelo penúltimo
    odd_sum = 0      # Armazena os demais dígitos

    for i in range(len(num) - 2, -1, -2):   # Do penúltimo dígito ao primeiro (índex 0) com espaço de 2
        if int(num[i]) * 2 > 9:             # Verifica se o número possui dois dígitos
            converter = str(int(num[i]) * 2)[0:2]
            pair_sum += int(converter[0]) + int(converter[1])
        else:
            pair_sum += int(num[i]) * 2

    for i in range(len(num) - 1, -1, -2):   # Do último dígito ao primeiro (índex 0) com espaço de 2
        if int(num[i]) * 2 > 9:             # Verifica se o número possui dois dígitos
            converter = str(int(num[i]) * 2)[0:2]
            odd_sum += int(converter[0]) + int(converter[1])
        else:
            odd_sum += int(num[i]) * 2

    if (odd_sum + pair_sum) % 10 == 0:
        return True
    else:
        return False


card_num = int(input('Digite o número do cartão: '))

if validate_card(card_num):
    id_card(card_num)
else:
    print('INVÁLIDO\n')
