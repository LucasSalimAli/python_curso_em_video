#Crie um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
n = int(input("Digite um número inteiro(sem virgulas): "))
ant = n-1
suc = n+1
print("Analisando o número: {0}, seu sucessor é: {1} e seu antecessor é: {2}.".format(n,suc,ant))