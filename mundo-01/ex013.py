#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input("Digite o seu salário atual: "))
au = (s*15)/100
print("Com 15% de aumento, seu salário será de R$:{0:.2f}, você recebeu um bônus de R$:{1:.2f}, parabéns!".format((s+au), au))