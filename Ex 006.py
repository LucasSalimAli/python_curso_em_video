#Crie um algorítimo que leia um número e mostre seu dobro, seu triplo e sua raiz quadrada.

n = int(input("Digite um número: "))
print("O dobro de {0} é: {1}, seu triplo é: {2}, e sua raiz quadrada é: {3}!".format(n, (n*2), (n*3), (n**(1/2))))