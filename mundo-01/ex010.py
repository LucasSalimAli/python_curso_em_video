#Crie um programa que leia quanto dinheiro a pessoa tenha na carteira, e mostre quantos dólares ela pode comprar.

n = float(input("Nos diga quanto dinheiro você tem na sua carteira, e iremos dizer quantos dolares você pode comprar: "))
d = 5.13

print("Com: R$:{0}, você poderá comprar cerca de: US$:{1:.2f}".format(n, (n/d)))