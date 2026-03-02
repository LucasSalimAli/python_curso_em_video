#Escreva um programa que converta uma temperatura em Cº e tranforme em Fº

t = float(input("Digite um valor em Cº e eu irei converte-lo em Fº: "))

print("A temperatura em Fº correspondente a {0}Cº é de: {1}".format(t, ((t * 1.8)+32)))