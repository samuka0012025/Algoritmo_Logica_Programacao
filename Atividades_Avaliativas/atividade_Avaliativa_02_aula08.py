# nome: Samuel da Silva
nome = "Samuel da Silva" 
# RA: 0220482523022
ra = "0220482523022"
print(f"Nome:{nome}\nRA:{ra}.")


valor = float(input("Por favor informe o valor da glicose em jejum! "))

if valor < 100:
    print("Glicemia normal")
elif valor >= 100 and valor < 125:
    print("Pré-Diabetes: Risco Moderado")
elif valor > 125:
    print("Diabetes: Nível Alto")
else:
    print("Vai ao médico, a coisa ta feia!")