def uniao(conj1, conj2):
    listaResultado1 = []
    for a in conj1:
        listaResultado1.append(a)
    for a in conj2:
        if a not in listaResultado1:
            listaResultado1.append(a)
    return listaResultado1

def interseccao(conj1, conj2):
    listaResultado2 = []
    for a in conj1:
        if a in conj2:
            listaResultado2.append(a)
    return listaResultado2

def diferenca(conj1, conj2):
    listaResultado3 = []
    for a in conj1:
        if a not in conj2:
            listaResultado3.append(a)
    return listaResultado3


def produtoCartesiano(conj1, conj2):
    listaResultado4 = []
    aux = ''
    for a in conj1:
        for b in conj2:
            aux = ('({0},{1})'.format(a,b))
            listaResultado4.append(aux)
    return listaResultado4


def complemento(conjU, conj1):
    listaResultado5 = []
    for a in conjU:
        if a not in conj1:
            listaResultado5.append(a)

    return listaResultado5


def uniaoDisjunta(silva, sousa):
    listaResultado6 = []
    for a in silva:
        aux = []
        aux.append(a)
        aux.append('Silva')
        listaResultado6.append(aux)
    for b in sousa:
        if b not in silva:
            aux = []
            aux.append(b)
            aux.append('Sousa')
            listaResultado6.append(aux)
    return listaResultado6


conj1 = [1, 2, 3, 4]
conj2 = [1, 2, 5, 6, 7]

silva = ['João', 'Maria', 'Jose']
sousa = ['Pedro', 'Ana', 'Jose']


