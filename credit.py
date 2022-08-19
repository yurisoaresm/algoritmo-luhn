# Função que identifica a bandeira do cartão (NOTA: apenas Visa, Mastercard ou American Express)
def id_card(num):
    if str(num)[0] == '4':
        print('VISA\n')
    else:
        if str(num)[0:2] in ['34', '37']:
            print('AMEX\n')
        elif str(num)[0:2] in ['51', '52', '53', '54', '55']:
            print('MASTERCARD\n')
        else:
            print('INVÁLIDO\n')


# Função que valida o número do cartão
def validate_card(num):
    # Declaração de variáveis para armazenar os dígitos pares (do penúltimo ao primeiro)
    # e ímpares (demais) e conversão do número para String
    num = str(num)
    pair_sum = 0
    odd_sum = 0

    # Aqui está o Algoritmo de Luhn propriamente dito
    # Soma o dobro dos dígitos do penúltimo ao primeiro
    for i in range(len(num) - 2, -1, -2):
        if int(num[i]) * 2 > 9:  # Verifica se o número possui dois dígitos e aplica a técnica de subtração por 9
            pair_sum += int(num[i]) * 2 - 9
        else:
            pair_sum += int(num[i]) * 2

    # Soma os demais dígitos e verifica se a soma é múltipla de 10
    for i in range(len(num) - 1, -1, -2):
        odd_sum += int(num[i])

    if (odd_sum + pair_sum) % 10 == 0:
        return True
    else:
        return False


card_num = int(input('Digite o número do cartão (apenas cartões Visa, American Express ou Mastercard): '))

if validate_card(card_num):
    id_card(card_num)
else:
    print('INVÁLIDO\n')
