aluno = {
    "matricula": 20261144010045,
    "nome": "Leticia",
    "curso": "Informatica",
    "idade": 17 }
# print(f"Curso: {aluno['curso']}")
# print(f"Fone: {aluno['fone']}") erro, não existe a chave telefone

for chave in aluno:
    print(f"{chave} => {aluno[chave]}")
