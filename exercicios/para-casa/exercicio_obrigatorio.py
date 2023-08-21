# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                          Até 5 Kg           Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou
# o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
# a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# calculando o custo de morangos
quantidade_morangos = float(input("Insira a quantidade de morangos, em kg: "))

if quantidade_morangos <= 5:
        preco_morangos = 2.5
else: preco_morangos = 2.2 

# calculando o custo de maçãs
quantidade_macas = float(input("Insira a quantidade de maçãs, em kg: "))

if quantidade_macas <= 5:
        preco_macas = 1.8
else: preco_macas = 1.5 

valor_compra = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas) 

# aplicando desconto
if (quantidade_macas + quantidade_morangos) > 8 or valor_compra > 25:
  preco_final = (valor_compra * 0.9)
else: preco_final = valor_compra

# imprimindo o valor arredondado
print("O valor a ser pago pelo cliente é de ", round(preco_final, 2), "reais.")