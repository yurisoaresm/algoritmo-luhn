# Problem Set 1
Este *problem set* é uma das tarefas a serem entregues no *pset* da primeira semana do curso de introdução à Ciência da Computação da **Harvard University** ([Harvard CS50](https://cs50.harvard.edu/x/2022/psets/1/ "Problem Set 1, Harvard CS50").): um validador de cartões de crédito com o **Algoritmo de Luhn**.

Este trabalho é individual, seguindo as **regras de integridade acadêmica** do [MIT](https://integrity.mit.edu/ "Academic Integrity at MIT") e de [Harvard](https://cs50.harvard.edu/college/2022/spring/syllabus/#academic-honesty "Academic Honesty at Harvard CS50"), 

**Feito por**: [Yuri Soares](https://github.com/yurisoaresm "Perfil do Yuri Soares no GitHub"),

E **orientado** por: [prof. Abrantes Araújo S. Filho](https://github.com/abrantesasf "Perfil do prof. Abrantes Araújo S. Filho no GitHub").

Este documento README explica como o projeto foi implementado e como executá-lo.

## 1 Algoritmo de Luhn e a Função validate_card()
Um cartão de crédito possui um código numérico de identificação que está impresso nele e armazenado em um banco de dados em algum lugar, de modo que o emissor de uma cobrança saiba para quem enviá-la.

Como muitas pessoas possuem pelo menos um cartão de crédito, o seu número é bem grande (ou seja, maior número de combinações possíveis) e todos os dígitos são algarismos de 0 a 9. Nesse sentido, é importante garantir um nível de segurança nos cartões, detectando erros (como transposições) ou até fraudes. Caso, para isso, fosse necessário sempre acessar um banco de dados para validar um número esse processo seria muito lento. Para tanto, todos os cartões possuem um **_checksum_** incorporado que se trata de uma relação matemática entre os dígitos do cartão.

A maioria dos cartões usa esse *checksum* para validar os números. Esse resultado é obtido por um algoritmo inventado por [Hans Peter Luhn](https://en.wikipedia.org/wiki/Hans_Peter_Luhn "Hans Peter Luhn, biography"), da IBM. A função **validade_card()** aplica diretamente o conceito do algoritmo de Luhn.

### 1.1 validade_card()
Essa função recebe o número do usuário e pega cada algarismo, começando pelo penúltimo e indo de 2 em 2 até o primeiro, multiplicando cada um por 2 e soma **todos os dígitos**. Caso a produto de um deles seja maior que 9, somamos os dígitos desse número.¹ Após isso, adicionamos a soma dos outros dígitos que não foram incluídos

> ¹ Como o maior algarismo de cada dígito é o 9, e seu dobro é 18, é possível fazer a soma dos algarismos dos números de dois dígitos usando a subtração por 9. Por exemplo: 10 -> 1 + 0 = 1 e 10 - 9 = 1, 16 -> 1 + 6 = 7 e 16 - 9 = 7, 18 -> 1 + 8 = 9 e 18 - 9 = 9. Perceba que isso é válido para qualquer número n tal que 9 < n < 19.

Feito isso, verificamos se o último dígito dessa soma é 0 (ou seja, se o número é divisível por 10). Caso sim, o número do cartão é válido. Em contrapartida, será inválido.²

> ² No escopo **deste projeto** estamos trabalhando apenas com cartões da **Visa**, **American Express** ou **Mastercard**; portanto, o algoritmo de Luhn não será o único método para validar um cartão. Os números seguem um padrão que deve ser atendido conforme explicado no tópico seguinte.

## 2 Identificação da Bandeira e a função id_card()
Os cartões **Visa** utilizam 13 ou 16 dígitos e começam com o número 4; **Mastercards** possuem 16 dígitos e os primeiros dígitos são 51, 52, 53, 54 ou 55; e **American Express** 15 dígitos, começando com 34 ou 37. Como esse é o contexto do nosso projeto, caso um número inserido pelo usuário não atenda a esses requisitos, ainda que o algoritmo de Luhn valide o cartão pela sua relação matemática, a saída será **inválida**.

A função id_card() verifica essas condições e imprime a bandeira do cartão.

## 3 Entrada do usuário e a função get_card()
A primeira função a ser chamada é a get_card(). Seu objetivo é receber o *input* do usuário e fazer o **tratamento de exceções** caso o usuário insira um valor diferente do esperado (inteiro); além disso, ignora os espaços que possam ter entre os dígitos. 

Essa função só retornará o dado de entrada caso nenhuma exceção ocorra.

## 4 Saída (*output*) do Programa
A única saída que será impressa no final do programa será AMEX\n (para cartões American Express), VISA\n, MASTERCARD\n ou INVÁLIDO\n.

### 4.1 Implementação 
O programa pode ser executado conforme os exemplos abaixo:

    $ python path/credit.py
    Digite o número do cartão apenas Visa, American Express ou Mastercard e sem hifens): 4222222222222
    VISA

    $ python credit.py
    Digite o número do cartão apenas Visa, American Express ou Mastercard e sem hifens): 371449635398431
    AMEX

    $ python credit.py
    Digite o número do cartão apenas Visa, American Express ou Mastercard e sem hifens): 1111111111111
    INVÁLIDO