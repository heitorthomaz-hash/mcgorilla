vogais=['a', 'e', 'i', 'o', 'u']
cont=0
palavra=str(input("Digite uma palavra: "))
for letra in palavra:
    if letra in vogais:
        cont+=1
print(f"O que fora digitado possui {cont} vogais")