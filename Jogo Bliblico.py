input('\nTecle <ENTER> ')


print ('\n'*100)
numjust = 50
while numjust >= 10:
    justos = input('Eu: ')
    try:
        if int(justos[20:23]) == numjust:
            print ("Deus: Nao destruirei a cidade por amor dos",numjust,"justos.")
            if numjust < 45:
                numjust -= 5
            numjust -= 5

        elif int(justos[20:23]) > numjust:
            print ("Deus: Voce nao deveria pedir por menos justos?")

        elif int(justos[20:23]) < numjust:
            print ("Deus: Voce nao gostaria de pedir por mais justos?")

    except ValueError:
        print ("Deus: Acaso vou destruir as cidades sem consultar Abraao?")
        numjust = 50
input('\nTecle <ENTER> ')


print ('\n'*100)
print ("\nDeus: Anjos, tirem Lo e sua familia de la...")
print ("\nAnjos: Sim, Senhor!")
print ("\n\n*** GAME OVER!!! ***\n")
input('\nTecle <ENTER> ')
