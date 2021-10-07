
def quantidade_de_letras (palavra) :
    quantidade = len (palavra)
    return quantidade


a = input ('Digite uma palavra...     ')
b = input ('Digite outra palavra...     ')


if quantidade_de_letras (a) > quantidade_de_letras (b):
    print("A menor palavra eh" .format(b))
elif quantidade_de_letras (a) == quantidade_de_letras (b):
    print("As duas palavras tem a mesma quantidade de letras")
else:
    print("A menor palavra eh" .format(a))

sair = input ('Tecle <ENTER> para encerrar...')
