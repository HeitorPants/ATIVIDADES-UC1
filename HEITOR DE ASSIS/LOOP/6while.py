#1-Um programa que mostre os números de 1 até 10.
numero = 1
while numero <=10:
    print(numero)
    numero += 1
print("fim")    
#2-Um programa que mostre os números de 10 até 1.
numero = 10
while numero >= 1:
    print(numero)
    numero = numero - 1
print("fim") 
#3-Um programa que mostre somente os números pares entre 1 e 20.
numero = 0
while numero <= 20:
    print(numero)
    numero % 2 == 0
    numero += 1
print("fim") 
#4-Um programa que solicite uma senha até o usuário informar "python123".
senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")

print("Acesso Permitido")
print("fim") 