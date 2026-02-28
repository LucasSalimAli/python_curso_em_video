#Faça um algorítimo que leia o preço de um prduto e mostre seu novo preço, com 5% de desconto.

p = float(input("Digite o preço do produto e irei dizer seu desconto: "))

d = (5*p)/100

print("Aplicando um desconto de 5%, o preço do produto será de {0}, você economizou {1}!".format((p-d), d))