
candidatos = range(2,100)
base = 2
num = base
resultado = [1]

while candidatos:
    while num < 100:
        if num in candidatos:
            candidatos.remove(num)
            
        num = num + base

    base = candidatos[0]
    num = base
    resultado.append(candidatos[0])
    del candidatos[0]

print(OS NUMEROS PRIMOS ENTRE 1 E 100!!!)
print(resultado)
