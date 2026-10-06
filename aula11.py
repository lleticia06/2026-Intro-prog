linguagens = {"python", "java", "c", "java"}
print (linguagens)
# {conjunto} [lista]
print (f"java-> {"java" in linguagens}")
# esta ou não no conjunto

numeros = set([6,7,8,9])
print (numeros)

letras = set("leticia")
print (letras)

vazio = set()
print (vazio)

tecnologias = {"python", "c"}
tecnologias.add("java")
tecnologias.update(["HTML", "CSS"])
print(tecnologias)
# add - um, update - vários. sorted - organiza.

cores = {"roxo", "azul", "verde"}
cores.discard("cinza") #sem erro que nn existe
cores.remove("verde")

print(sorted(cores))

time = {"leticia", "luiza", "lais"}
time.pop()
print(time)

compras = {"arroz", "cuscuz", "tomate"}
compras.clear()
print(compras)

nome = set("leticia")
print(sorted(nome))

A = {6,7,0}
B = {4,8,1}
print(A| B, A & B)