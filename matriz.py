def matriz_nula(nlinhas, ncols):
    M = []
    for i in range(nlinhas):
        linha = [0]*ncols
        M.append(linha)
    return M

def transposta(M):
    nlinhas = len(M)
    ncolunas = len(M[0])
    T = matriz_nula(ncolunas, nlinhas)
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = M[i][j]
    return T

def eh_igual(A, B):
    nlinhasA, ncolunasA = len(A), len(A[0])
    nlinhasB, ncolunasB = len(B), len(B[0])
    if (nlinhasA == nlinhasB) and (ncolunasA == ncolunasB):
        for i in range(nlinhasA):
            for j in range(ncolunasA):
                if A[i][j] != B[i][j]:
                    return False
        return True
    
    return False

def somar(A, B):
    C = []
    nLinhasA, nLinhasB = len(A), len(B)
    nColA, nColB = len(A[0]), len(B[0])
    if (nLinhasA == nLinhasB) and (nColA == nColB):
        for i in range(nLinhasA):
            linha = [0]*nColA
            C.append(linha)
            for j in range(nColA):
                C[i][j] = A[i][j] + B[i][j]
    else:
        print("Matrizes não tem a mesma ordem")

    return C

def oposta(M):
    op = []
    for i in range(len(M)):
        linha = [0]*len(M[0])
        op.append(linha)
        for j in range(len(M[0])):
            op[i][j] = -M[i][j]
    return op

def subtrair(A, B):
    return somar(A, oposta(B))

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def ler_matriz(arquivo):
    matriz = []
    arquivo = open(arquivo, "r")
    linha = arquivo.readline()
    while linha!= "":
        elementos = linha.split()
        for n in range(len(elementos)):
            elementos[n] = int(elementos[n])
        matriz.append(elementos)
        linha = arquivo.readline()
    arquivo.close()
    return matriz


if __name__ == "__main__":
    m = int(input("Número de linhas: "))
    n = int(input("Número de colunas: "))

    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = input("Elemento da linha {} e coluna {}".format(i, j))
            linha.append(int(elemento))
        matriz.append(linha)

    exibir_matriz(matriz)
    matriz = ler_matriz()
    exibir_matriz(matriz)
