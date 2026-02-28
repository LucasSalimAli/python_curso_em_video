#Faça um programa que leia a largura ea a altura de uma parede em metros, e calcule sua área e a quantidade de tinta necessária para printa-la. Considerando que cada litro de tinta pinte um área de 2m²

l = float(input("Digite a Largura da sua parede: "))
a = float(input("Digite a altura da sua parede: "))

print("A área da sua parede é de: {0}m², e você terá que usar cerca de {1} latas de tinta.".format((l*a), ((l*a)/2)))