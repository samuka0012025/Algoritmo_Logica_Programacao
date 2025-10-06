# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")

peso = float(input("Por favor informe o peso da encomenda! (KG) "))
distancia = int(input("Por favor informe por gentileza a distância de entraga! (KM) "))

custo = (peso * 1.5) + (distancia * 0.25)

if custo > 200:
    desc10 = custo * (10 / 100) 
    val_final = custo - desc10
    print(f"Custo base original: R${custo}\nCusto final: R${val_final}")
elif custo >= 50 and custo < 200:
    print(f"Custo base original: R${custo}\nCusto final: R${custo}")
else:
    print(f"Custo base original: R${custo}\n + Taxa de manuseio: R$ 5,00\n Custo final: R${custo + 5.00}")
