#rie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input("Digite Algo: ")
print("Isso é do tipo: ", type(a))
print("Só possui espaços? ", a.isspace())
print("Só possui número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("Está em CapsLock? ", a.isupper())
print("Só tem minúsculas? ", a.islower())
print("O Tamanho é: ", len(a))