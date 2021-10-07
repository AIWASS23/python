import math

tipo = 0
comodos = []
while (tipo != -1):
    lista = []
    tipo = int(input("Informe o tipo do cômodo: "))
    if tipo != -1:
        larg = float(input("Informe a largura do cômodo: "))
        comp = float(input("Informe o comprimento do cômodo: "))
        lista.append(tipo)
        lista.append(larg)
        lista.append(comp)
        comodos.append(lista)

print(lista)
lista = 1
print(lista)
pot = [12,15,18,20,22,25]
for x in comodos:
    area = x[1]*x[2]

    print("São necessários ",area*pot[x[0]]," W para iluminar este cômodo")
    print("Portanto ",math.ceil((area*pot[x[0]])/60)," lâmpada(s)")

    
