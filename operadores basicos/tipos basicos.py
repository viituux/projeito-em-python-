inteiro  = 10  # int = (numero inteiro )
decimal = 10.0 # float = (numero decimal)
complexo = 3 + 4j # complex = ( numero complexo)

print( inteiro , decimal , complexo)
print(f"TIPOS: {type(inteiro )}, {type(decimal)} , {type(complexo)}" )

# TEXTO 
Texto = "ola, mundo" #string (string / texto )
print(Texto)
print(f"TIPOS: {type(Texto)}") 
 
# booleanos 

verdadeiro = True #  bool ( booleando  verdadeiro )
falso = False # bool ( booleando falso )

print(verdadeiro , falso )
print(f"Tipos: {type(verdadeiro)} {type(falso)}")

# colecoes 

lista= [1,2,3] # list (lista mutavel)
lupla= (1,2,3) # lupla (lupla imutavel)
dicionario = {"nome": "joao"} # dict (dicionario)
conjuntos = {1,2,3} #set (dicionario)

print(lista,lupla,dicionario,conjuntos)
print(f"tipos:{type(lista)},{type(lupla)},{type(dicionario)},{type(conjuntos)}")

# COMANDO INPUT 

Nome = input("digite seu nome :")
print(f"ola, {Nome}! bem- vindo ao python ")
idade= int(input("digite sua idade : "))
print(f"daqui a 5 anos voce tera, {idade + 5 } anos" )

altura = float(input("digite sua altura:"))
print(f"sua altura é de : {altura}, metros  ou a {altura + 100 } centimetros  ")