#Declarando variaveis e setando seus valores

nome = input("O nome da pessoa")

a = input("Valor da variavel a")
b = input("Valor da variavel b")

soma = a + b

#Condições
if(soma > a):
    print('É maior que a')
elif(soma == a):
    print('É igual')
else:
    print('Outra condição')


print(nome + ", nome completo")
print(nome[0]+ ", primeira letra")
print(nome[1]+ ", segunda letra")