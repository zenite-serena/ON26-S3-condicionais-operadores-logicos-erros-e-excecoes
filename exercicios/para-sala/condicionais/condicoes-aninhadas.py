nota = 6
presenca = 60

if nota >= 7 or presenca == 100:
    print("Aprovado!")
elif nota < 7 and nota > 5: 
    if presenca >= 90: 
        print("Aprovado!")
    elif presenca > 50:
        print("Apto a fazer recuperação")
    else:
        print("Reprovado") 
else:
    print("Reprovado")

print("Fim do Programa")