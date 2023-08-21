#Exercícios de Estrutura de Decisão #1-10

#1. Faça um Programa que peça dois números e imprima o maior deles. 

numero1 = float(input("Insira o valor do primeiro número: "))
numero2 = float(input("Insira o valor do segundo número: "))

if numero1 > numero2:
    print("O maior número é ", numero1)
elif numero2 > numero1:
    print("O maior número é ", numero2)
else: print("Os números são iguais")

print("Fim do programa 1")

#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

numero = float(input("Insira o número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else: print("O número é igual a zero")

print("Fim do programa 2")

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

print("Informe o sexo no campo a seguir")
print("F para feminino, M para masculino ou N/A para não informar")

sexo = input("Sexo: ")

if sexo == "f" or sexo == "F":
    print("Sexo feminino")
elif sexo == "m" or sexo == "M":
    print("Sexo masculino")
else: print("Sexo não informado")

print("Fim do programa 3")

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

letra = str(input("Digite uma letra: "))

if letra == "a" or letra == "e" or letra == "i" or  letra == "o" or  letra == "u" or letra == "A" or letra == "E" or letra == "I" or  letra == "O" or  letra == "U":
    print("A letra é uma vogal")
else: print("A letra é uma consoante")

print("Fim do programa 4")

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
## A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
## A mensagem "Reprovado", se a média for menor do que sete;
## A mensagem "Aprovado com Distinção", se a média for igual a dez. 

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2)/2

if media == 10:
    print("Aprovada com mérito")
elif media >= 7:
    print("Aprovada")
else: print("Reprovada")

print("Fim do programa 5")

# 6. Faça um Programa que leia três números e mostre o maior deles. 

numero1 = float(input("Insira o valor do primeiro número: "))
numero2 = float(input("Insira o valor do segundo número: "))
numero3 = float(input("Insira o valor do terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é ", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("O maior número é ", numero3)
elif numero1 == numero2 == numero3:
    print("Os números são iguais")

print("Fim do programa 6")

# 7. Faça um Programa que leia três números e mostre o maior e o menor deles. 

numero1 = float(input("Insira o valor do primeiro número: "))
numero2 = float(input("Insira o valor do segundo número: "))
numero3 = float(input("Insira o valor do terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("O maior número é ", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("O maior número é ", numero3)
elif numero1 == numero2 == numero3:
    print("Os números são iguais")

if numero1 < numero2 and numero1 < numero3:
    print("O menor número é ", numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("O menor número é ", numero2)
elif numero3 < numero1 and numero3 < numero2:
    print("O menor número é ", numero3)

print("Fim do programa 7")

# 8. Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato. 

nome_produto1 = str(input("Insira o nome do primeiro produto: "))
produto1 = float(input("Insira o valor do primeiro produto: "))
nome_produto2 = str(input("Insira o nome do segundo produto: "))
produto2 = float(input("Insira o valor do segundo produto: "))
nome_produto3 = str(input("Insira o nome do terceiro produto: "))
produto3 = float(input("Insira o valor do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print("O cliente deve comprar", nome_produto1)
elif produto2 < produto1 and produto2 < produto3:
    print("O cliente deve comprar", nome_produto2)
elif produto3 < produto1 and produto3 < produto2:
    print("O cliente deve comprar", nome_produto3)
elif produto1 == produto2 == produto3:
    print("Não há diferença de preço")

print("Fim do programa 8")

# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente. 

numero1 = float(input("Insira o valor do primeiro número: "))
numero2 = float(input("Insira o valor do segundo número: "))
numero3 = float(input("Insira o valor do terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3 and numero2 >= numero3:
    print("A ordem decrescente é: ", numero1, ",", numero2, ",", numero3)
elif numero1 >= numero2 and numero1 >= numero3 and numero3 >= numero2:
    print("A ordem decrescente é: ", numero1, ",", numero3, ",", numero2)
elif numero2 >= numero1 and numero2 >= numero3 and numero3 >= numero1:
    print("A ordem decrescente é: ", numero2, ",", numero3, ",", numero1)
elif numero2 >= numero1 and numero2 >= numero3 and numero1 >= numero3:
    print("A ordem decrescente é: ", numero2, ",", numero1, ",", numero3)
elif numero3 >= numero2 and numero3 >= numero1 and numero2 >= numero1:
    print("A ordem decrescente é: ", numero3, ",", numero2, ",", numero1)
elif numero3 >= numero2 and numero3 >= numero1 and numero1 >= numero2:
    print("A ordem decrescente é: ", numero3, ",", numero1, ",", numero2)

print("Fim do programa 9")

# 10. Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. 

print("Informe o período conforme a legenda:")
print("M - Matutino, V - Vespertino, N - Noturno")
periodo = input("Período: ")

if periodo == "M" or periodo == "m":
    print("Bom dia!")
elif periodo == "V" or periodo == "v":
    print("Boa tarde!")
elif periodo == "N" or periodo == "n":
    print("Boa noite!")
else: print("Valor inválido!")

print("Fim do programa 10")
