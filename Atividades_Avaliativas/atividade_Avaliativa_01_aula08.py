# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"

print(f"Nome:{nome}\nRA:{ra}.")

# Solicitando ao usuário
preco_custo = float(input("Por favor, informe o valor do preço de custo! "))
preco_venda = float(input("Por favor, informe o valor do preço de venda! "))

# Calculando o lucro absoluto
lucro = preco_venda - preco_custo 

# Calculando a margem de lucro em porcentagem
margem = (lucro / preco_custo) * 100

# Verificando as classificações a margem de lucro
if margem > 30:
    print("Margem Excelente!")
elif 10 < margem < 30:
    print("Margem satisfatória!")
else:
    print("Margem baixa: Avaliar preço de venda.")

