print("Calculo para Euclides")

a = 0
b = 0
calc = 1
f1 = 0
f3 = 0

def testar(v1,v2):
    if v1 > v2:
        resp_testar = 1
    elif v1 == v2:
        resp_testar = 2
    else:
        resp_testar = 0
        
    return resp_testar
        
def novo(decisao):
    print("Deseja reiniciar seu cauculo?")
    print("Digite 1 para sim ou 0 para nao.")
    decisao = input("> ")
    while decisao < 0 or decisao > 1:
        print("Deseja reiniciar seu cauculo?")
        print("Digite SOMENTE 1 para sim ou 0 para nao!")
        decisao = input("> ")

    return decisao

def euclides(v1, v2):
    v1,v2 = v2, a%b
    while not v2 == 0:
        v1,v2 = v2, v1%v2
        
    return v1
        
while calc == 1:
    a = input("Digite o primeiro numero : > ")
    b = input("Digite o segundo numero : > ")
    f1 = testar(a,b)
    if f1 == 0:
        print("Seu segundo valor tem que ser menor que o primeiro!")
        calc = novo(calc)
        print(calc)
    elif f1 == 2:
        print("Seu segundo valor nao pode ser igual ao primeiro!")
        calc = novo(calc)
        print(calc)
    else:
        f3 = euclides(a,b)
        print("O fator comum entre",a,b,"eh",f3,"!!!")
        calc = novo(calc)            

print("Calculo Finalizado")