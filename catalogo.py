equipamentos = []
preços = []
numero_de_serie = []
departamentos = []
inventario = []
resposta ="S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    preços.append(float(input("Valor: ")))
    numero_de_serie.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", preços[indice])
    print("Serial.......: ", numero_de_serie[indice])
    print("Departamento.: ", departamentos[indice])

busca = input("\n Digite o nome do equipamento que deseja buscar: ")

for indice in range(0,len(equipamentos)):
     if busca==equipamentos[indice]:
        print("Valor..: ", preços[indice])
        print("Serial.:", numero_de_serie[indice])

novo_preço = input("\n Digite o nome do equipamento que será depreciado: ")

for indice in range(0,len(equipamentos)):
    if novo_preço == equipamentos[indice]:
        print("Valor antigo: ", preços[indice])
        preços[indice] = preços[indice] * 0.9
        print("Novo valor: ", preços[indice])

numero_de_serie = int(input("\n Digite o serial do equipamento que será excluido: "))

for indice in range(0, len(departamentos)):
    if numero_de_serie[indice] == numero_de_serie:
        del departamentos[indice]
        del equipamentos[indice]
        del numero_de_serie[indice]
        del preços[indice]
        break

for indice in range(0,len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", preços[indice])
    print("Serial.......: ", numero_de_serie[indice])
    print("Departamento.: ", departamentos[indice])

valores = []
for elemento in inventario:
    valores.append(elemento[1])

if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))

