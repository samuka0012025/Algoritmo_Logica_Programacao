# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")

C_inicial = float(input("Informe o custo inicial do material: "))
q = int(input("Por favor informe a quantidade de itens produzidos: "))
dias = int(input("Informe o número de dias de atraso: "))
defeito = float(input("Qual foi o percentual de defeitos? "))

if q > 1000 and C_inicial > 5000:
    F_comp = 1.15
else:
    F_comp = 1.05

C_corrigido = C_inicial * F_comp

if defeito > 0.10 or dias > 5:
    print(f"Penalidade Alta: 20% de redução no lucro")
    C_final = C_corrigido * 1.25
elif (defeito >= 0.05 and defeito < 0.10) and (dias > 0):
    print(f"Penalidade Média: 10% de redução no lucro")
    C_final = C_corrigido * 1.10
else:
    print(f"Sem penalidade. Custo final apenas com correção")
    C_final = C_corrigido 

print(f"Custo Base Corrigido: R${C_corrigido}\nCusto final do lote: R$ {C_final}")
    
