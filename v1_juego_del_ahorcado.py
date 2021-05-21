# Elaborar un juego del ahorcado
# |Reglas|
# Incorpora comprehensions, manejo de errores y manejo de archivos
# Utiliza el archivo data.txt y leelo para obtener las palabras
# |Ayudas|
# Investigar funcion enumerate()
# El metodo get de los diccionarios puede servirte
# La sentencia os.system("cls") te servira para limpiar la pantalla
# |Mejora el juego|
# Añade un sistema de puntos
# Dibuja al ahorcado en cada jugada con codigo ASCII
# Mejora la interfaz
import random
import os

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "ae"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def print_word(word, guessed_letters):
    """Esta funcion va a imprimir una cantidad len(word)
       de guiones bajos, y cuando se adivine una o mas 
       letra(s), se van a reemplazar los guiones bajos
       por las letra(s) adivinada(s) en su(s) respectivo(s)
       lugar(es).

       word -- string -- palabra a adivinar
       guessed_letters -- list -- lista de letras que se adivinaron de word
       
    """
    counter = 1
    for letter in word:
        if letter != '\n':
            if guessed_letters.__contains__(letter):
                print(letter, end=' ')
                counter = counter + 1
            else:
                print("_", end=' ')
    if counter == len(word):
        return True
    else:
        return False
    

def random_word():
    """Selecciona una palabra aleatorio del archivo data.txt.

       Abrimos una lista, recorremos el archivo data.txt y guardarmos
       en nuestra lista una linea al azar y la devuelve.

    """
    words = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        for counter, line in enumerate(f):
            words.append(line)
    selected_word = words[random.randint(0, counter)]       
    return selected_word


def letter_input(letter):
    """Optimiza la letra ingresada.

    Se procesa la letra ingresada por el usuario

    Parametros:
    letter -- Letra ingresada por el usuario
    
    """
    try:
        if letter.isnumeric() == True or len(letter) != 1 or letter == "" or letter == " ":
            raise ValueError
        letter = letter.strip()
        letter = letter.lower()
        return letter
    except ValueError as ve:
        os.system('cls')
        print('\nNo se pueden ingresar numeros, ni mas de un letra.\n')
        return False


def save_word_letters(word):
    letters_to_guess = []
    for letter in word: #Guarda las letras de la palabra en una lista
        if letter == '\n':
            continue
        letters_to_guess.append(letter)
    return letters_to_guess


def run():
    
    lifes = 6
    guessed_letters = []
    already_said_letters = []
    word_to_guess = normalize(random_word())
    letters_to_guess = save_word_letters(word_to_guess)
    os.system('cls')
    print("Bienvenido al Ahorcado \n ------------\n")

    while lifes > 0 and print_word(word_to_guess, guessed_letters) == False:
        print('\n' + HANGMANPICS[6 - lifes])
        print('\n\nTienes ' + str(lifes) + ' vidas')
        choosed_letter = letter_input(input("\nIngresa una letra: \n"))

        if choosed_letter == False: 
            continue
        else:
            if letters_to_guess.__contains__(choosed_letter):
                guessed_letters.append(choosed_letter)
                os.system('cls')
                print("AHORCADO")
                print("\nAdivinaste una letra!\n")
                already_said_letters.append(choosed_letter)
                print('Ya dijiste las letras: ' + "".join(already_said_letters) + '\n')
            else:
                lifes = lifes - 1                                                                                                                  
                already_said_letters.append(choosed_letter)
                os.system('cls')
                print("AHORCADO")
                print("\nLa palabra no contiene esa letra")
                print('Ya dijiste las letras: ' + "".join(already_said_letters) + '\n')

    print('\n' + HANGMANPICS[6 - lifes])

    if lifes > 0:
        print("\n Ganaste!, te quedaban " + str(lifes) + " vidas")
    else:        
        print('\n\nPerdiste, la palabra era ' + word_to_guess)


if __name__ == '__main__':
    run()


