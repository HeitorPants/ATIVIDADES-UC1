produto = input("Digite o nome do produto: ")
valorproduto = float(input("Digite o valor do produto: "))
qtdproduto = int(input("Digite a quantidade do produto: "))
valortotal = valorproduto * qtdproduto
print(f"O valor da compra total de {qtdproduto} {produto} foi de R$ {valortotal} reais")