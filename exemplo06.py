idade = int(input("Qual sua idade: "))
if idade < 18:
    print(f"menor de idade")
else:
    print(f"Maior de idade")

# if ternário
print("Menor" if idade < 18 else "Maior")