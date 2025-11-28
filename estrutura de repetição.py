# #for
# #interando sobre uma lista
#
# frutas = ["maça","banana","cereja"]
# for fruta in frutas:
#     print(fruta)

# #interando range para repetir um bloco de codigo 5 vezes
# for i in range(1,11):
#     print("Contagem:", i)

#enumerate() é util para interar sobre uma sequencia e, ao mesmo tempo, manter um contador automatico (indice)

# for indice, valor in enumerate(sequecia, start=0):
#     #bloco de codigo a ser reproduzido

# frutas = ["maças","banana","cereja"]
# for indice, fruta in enumerate(frutas):
#     print(f"Fruta {indice}:{fruta}")

# cores = ["azul","verde","amarelo","vermelho"]
# for indice, cores in enumerate(cores):
#     print(f"Cores {indice}:{cores}")

# dinheiro = 50
# while dinheiro > 0:
#     print(f"voce ainda tem {dinheiro}")
#     dinheiro -= 10
# print("acabou dinheiro")

for i in range(1,21):
    # Condição de pular (continue)
    if i % 3 ==0:
        continue #se for divisivel por 3, volta ao inicio

    # Condição para parar (break)
    if i == 17:
        print("Chegamos ao 17. Parando o laço")
        break
    print(i)