# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")

pureza_lote = float(input("Qual foi a pureza do lote? "))
massa_total = float(input("Qual foi a massa total do lote? "))
taxa_conta = float(input("Qual foi a taxa de contaminação? "))

fd = (pureza_lote * 100) - (taxa_conta * 50)

if massa_total > 1000:
    P_base = 10.00
else:
    P_base = 12.50

if fd > 90 and pureza_lote > 0.98:
    print("Classificação: Premium (Venda Imediata)")
    p_final_kg = P_base * 1.50
elif (fd >= 70 and fd > 90) and (taxa_conta > 0.05):
    print("Classificação: Padrão (Venda Normal)")
    p_final_kg = P_base * 1.10
elif fd < 70 or pureza_lote < 0.90:
    print("Classificação: REPROVADO (Descarte ou RE-Processamento)")
    p_final_kg = P_base * 0.25
else:
    print("Classificação: ACEITÁVEL (Margem Mínima)")
    p_final_kg = P_base * 0.90

preco_total_final = p_final_kg * massa_total

print(f"Preço base por kg: R$ {P_base}\nPreço final total: R$ {preco_total_final}")

