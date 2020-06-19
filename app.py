from random import choice
from config import funcoes
from config import menu
center = 0

#==============================================================================================




# Variaveis auxiliares

error = 0

aux = "abcdefghijklmnopqrstuvwxyz-"
partes_do_corpo = [" ", " ", " ", " ", " ", " ", " "]
letras_usadas = ""

#Menu 

menu.main()

while True:
    tipo = int(input('Opção >  '))
    if (tipo == 1):
        
            # Categoria de animais 
        ani = ["raposa", "tubarao", "cobra", "jabuti", "baleia", "cachorro", \
            "gato", "peixe", "arraia", "alce", "pinguim", "rato", "avestruz", "macaco", \
            "boi", "vaca"]

        # Categoria de frutas
        fru = ["banana", "laranja", "uva", "morango", "manga", "melancia", "pera", \
            "jaca", "cereja", "goiaba", "acerola", "abacate", "cacau", "caqui", "carambola", \
            "groselha", "jabuticaba", "jambo", "kiwi", "amora", "abacaxi"]
        tipo = int(input('[1]Animais\n' '[2]Frutas'))

        if (tipo == 1):
            palavra = choice(ani)
            break
        elif (tipo == 2):
            palavra = choice(fru)
            break
        else:
            print('Opção incorreta, MONGOL!')

    elif (tipo == 2):
        palavra = input("Palavra > ").lower().replace(" ", "-")
        break
    else:
        print('Não existe essa opção, Mongoloide!')

letras_encontradas = "_" * len(palavra)
funcoes.atualizacoes(letras_usadas, center, partes_do_corpo, error, letras_encontradas)


# Codigo principal

while letras_encontradas != palavra and error < 7:
    try:
        letra = input(center * ' ' + 'Letra> ')[0].lower()
    except:
        letra = ''
    
    if (letra == ' '):
        letra = '-' 
    if (letra not in letras_usadas and letra in aux):
        letras_usadas += letra + ', '
        if (letra in palavra):
            letras_encontradas = funcoes.trocar_letra(palavra, letra, letras_encontradas)
        else:
            error += 1
    

        funcoes.atualizacoes(letras_usadas, center, partes_do_corpo, error, letras_encontradas)
funcoes.limpar()
if (error == 7):
    print("Você perdeu!")
else:
    print(center * " " + "Você ganhou!")
print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "A Palavra era", palavra, "\n" * 15)