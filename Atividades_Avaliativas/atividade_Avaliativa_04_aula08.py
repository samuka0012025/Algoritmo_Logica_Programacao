# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")


p = float(input("Por favor informe o valor inicial do investimento! "))
t = int(input("Por favor informe o prazo do investimento em meses! "))

if t < 6:
    j = 0.005
elif t >= 6 and t < 12:
    j = 0.008
else:
    j = 0.012

rendimento_total = p * j * t

print(f"Foi aplicado {j}%\nE seu rendimento total obtido foi R$ {rendimento_total:.2f}")