# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")


r_investimento = float(input("Informe o retorno do investimento: "))
r_livre = float(input("Informe qual é a taxa livre de risco: "))
sigma = float(input("Qual é o desvio padrão de volatilidade: "))

sharp = (r_investimento - r_livre) / sigma
spread = r_investimento - r_livre

if sharp % 2 != 0:
    if sharp > 1.5 and spread > 0.05:
        print("Investimento Excelente: Alta performance ajustado ao risco")
    elif sharp >= 0.5 and sharp < 1.5 or spread > 0.02:
        print("Investimento Bom: Risco e retorno moderados")
    elif sharp < 0.5 and r_investimento > 0:
        print("Investimento Aceitavel: Retorno positivo, mas risco alto para o ganho")
    else:
        print("Investimento Ruim: Não recomendado")
else:
    print("Não posso executar")

