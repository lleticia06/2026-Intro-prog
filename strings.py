# Analise de log
arquivo = open("log_acessos_1000_registros.txt", "r", )
#print(arquivo.read())
falhas = []
for linha in arquivo:
    if "FALHA" in linha:
        falhas.append(linha)
print(falhas)
print(f"Total de falhas = {len(falhas)}")
