"""
Title       : Problem Set 1: Algoritmo de Luhn
Description : Receber um número de cartão do usuário e verificar se o número é válido segundo o Algoritmo de
            : Luhn e identificar a sua bandeira (Visa, Mastercard ou American Express)

Author      : Yuri Soares (github.com/yurisoaresm)
Language    : Python
Version     : 3.10.6
"""


# Declaração de funções:
# Função que identifica a bandeira do cartão (NOTA: apenas Visa, Mastercard ou American Express)
def id_card(num):
    num = str(num)
    if num[0] == '4' and len(num) in [13, 16]:
        print('VISA\n')
    else:
        if num[0:2] in ['34', '37'] and len(num) == 15:
            print('AMEX\n')
        elif num[0:2] in ['51', '52', '53', '54', '55'] and len(num) == 16:
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


# Função que recebe o número do cartão e faz o tratamento de exceção
def get_card():
    flag = True
    while flag:
        try:
            card = int(input('Digite o número do cartão '
                             '(apenas Visa, American Express ou Mastercard e sem hifens): ').replace(' ', ''))
            flag = False
            return card
        except ValueError:
            print('Por favor, digite apenas números.')


# Chamada do programa
card_num = get_card()

if validate_card(card_num):
    id_card(card_num)
else:
    print('INVÁLIDO\n')
