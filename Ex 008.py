#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e em milímetros.

vm = float(input("Digite um valor em metros e eu irei converte-lo para centimetro e para milimetro: "))
print("O valor de: {0} metros em Centímetros é: {1} cm, e o valor em Milimetros é: {2} mm".format(vm, (vm*100), (vm*1000)))