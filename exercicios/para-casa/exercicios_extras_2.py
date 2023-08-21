#Exercícios de Estrutura de Decisão #11-12

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
# e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 

# Após o aumento ser realizado, informe na tela:
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento. 

# informando o valor do salário

salario = float(input("Informe o valor do salário atual, em reais: "))

# fazendo o reajuste

if salario <= 280:
    reajuste = 1.20
elif 280 < salario < 700:
    reajuste = 1.15
elif 700 < salario < 1500:
    reajuste = 1.10
elif 1500 < salario:
    reajuste = 1.05

salario_final = salario * reajuste

# calculando o percentual
# por algum motivo, se eu tento fazer
## percentual = reajuste - 1
# eu recebo um valor aproximado, com muitas casas decimais
# então vou fazer uma forma menos inteligente de calcular o percentual

if reajuste == 1.20:
    percentual = "20 por cento"
elif reajuste == 1.15:
    percentual = "15 por cento"
elif reajuste == 1.10: 
    percentual = "10 por cento"
elif reajuste == 1.05:
    percentual = "5 por cento"

# calculando o valor do aumento

valor_aumento = salario_final - salario

print("O salário inicial era de ", str(salario), "reais") 
print("Após o reajuste de ", percentual)
print("recebeu um aumento de", valor_aumento)
print("resultando no valor final de", str(salario_final)) 

print("Fim do programa 11")

# 12. Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) 
# e 10% para o INSS 
# e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    ## Desconto do IR:
    ## Salário Bruto até 900 (inclusive) - isento
    ## Salário Bruto até 1500 (inclusive) - desconto de 5%
    ## Salário Bruto até 2500 (inclusive) - desconto de 10%
    ##Salário Bruto acima de 2500 - desconto de 20% 

# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220. 

# Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valor_da_hora = float(input("Informe o valor da sua hora: "))
quantidade_horas = float(input("Informe a quantidade de horas trabalhadas: "))

# calculando o salário bruto

salario_bruto = valor_da_hora * quantidade_horas

# calculando o desconto do IR

if salario_bruto <= 900:
    percentual_ir = 0
elif 900 < salario_bruto <= 1500:
    percentual_ir = 0.05
elif 1500 < salario_bruto <= 2500:
    percentual_ir = 0.10
else: percentual_ir = 0.20
    
salario_desconto_ir = salario_bruto - (salario_bruto * percentual_ir)
desconto_ir = percentual_ir * 100

# calculando o desconto do INSS

percentual_inss = 0.10

salario_desconto_inss = salario_bruto - (salario_bruto * percentual_inss)

# calculando o valor do FGTS

percentual_fgts = 0.11
valor_fgts = (salario_bruto * percentual_fgts)

# calculando o salário líquido

salario_liquido = salario_bruto - (salario_bruto * percentual_ir) - (salario_bruto * percentual_inss)

# imprimindo os valores

print("Salário Bruto:", salario_bruto)
print("(-) IR (", desconto_ir, "%): R$", (salario_bruto * percentual_ir))
print("(-) INSS ( 10%): R$", (salario_bruto * percentual_inss))
print("FGTS (11%): R$", valor_fgts)
print("Total de descontos: R$", ((salario_bruto * percentual_ir) + (salario_bruto * percentual_inss)))
print("Salário Liquido: R$", salario_liquido)