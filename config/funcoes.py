
#Funcões

# limpar tela 
def limpar():
    print("\n" * 20)

# validar a letra na palavra 
def trocar_letra(palavra, letra, letras_encontradas):
    return_l = ""
    for p, l in enumerate(palavra):
        if ( l == letra ):
            return_l += l
        else:
            return_l += letras_encontradas[p]
    return return_l

# Mostras as letras encontradas 

def mostrar_letras_encontradas(center, letras_encontradas):
    print((center - len(letras_encontradas) + 5)*' ', end='')
    for l in letras_encontradas:
        print(l + ' ',end='')
    print('\n')

# Mostrar letras usadas

def letra_usada(letras_usadas, center):
    print('LETRAS USADAS')
    print((center - int(len(letras_usadas)/2) + 5) * ' ',end= ' ')
    for l in letras_usadas[0:-2]:
        print(l , end='')
    print('\n')

# Desenhas Boneco

def desenhar(partes_do_corpo, center, error):
    if (error == 1):
        partes_do_corpo[0] = '0' # Cerebro
    elif (error == 2):
        partes_do_corpo[1] = '|' # Peito
    elif (error == 3):
        partes_do_corpo[2] = '|' # Cintura
    elif (error == 4):
        partes_do_corpo[3] = '/' # Perna esquerda 
    elif (error == 5):
        partes_do_corpo[4] = ' \\' #Perna direita
    elif (error == 6):
        partes_do_corpo[5] = '/' # Braco esquerdo
    elif (error == 7):
        partes_do_corpo[6] = '\\' #Bracco direito

    print(center * " " + "   ____ ")
    print(center * " " + "  /    |")
    print(center * " " + " /     " + partes_do_corpo[0])
    print(center * " " + "|     " + partes_do_corpo[5] + partes_do_corpo[1] + partes_do_corpo[6])
    print(center * " " + "|      " + partes_do_corpo[2])
    print(center * " " + "|     " + partes_do_corpo[3] + partes_do_corpo[4])
    print(center * " " + "|")

# Atualizações no tabuleiro
def atualizacoes(letras_usadas, center, partes_do_corpo, error, letras_encontradas):
    letra_usada(letras_usadas, center)
    print( "<ESPAÇO IGUAL A HÍFEN>" + "\n" * 2)
    desenhar(partes_do_corpo, center, error)
    mostrar_letras_encontradas(center, letras_encontradas)