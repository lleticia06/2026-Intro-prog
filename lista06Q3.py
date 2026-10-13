#Estrutura: CONJUNTOS
lista = ["José", "Inácio", "Rosa", "José", "José", "Maria", "Rosa", 
         "Inácio", "José", "Maria", "José", "Rosa"]
inscritos = set(lista)
print(f"Quantidade de inscrições: {len(lista)}") 
print(f"Pessoas inscritas: {len(inscritos)}")
print(sorted(inscritos))
