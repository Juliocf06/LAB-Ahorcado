import random

def cargar_palabras(ruta):
    ''' 
    Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
    dichas palabras en una lista.    
    
    :param ruta: Ruta de un fichero de texto. El fichero debe contener una palabra por línea.
    :type ruta: str
    :return: Una lista con las palabras leías del fichero
    :rtype: list[str]
    '''
    
    with open(ruta, encoding='utf-8') as f:
        res = []
        for linea in f:
            res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
        return res

def elegir_palabra(palabras):
    return random.choice(palabras)

def enmascarar_palabra(palabra:str, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la cadena resultado 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena con la palabra enmascarada.
    
    :param palabra: Palabra que se quiere enmascarar
    :type palabra: str
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: La palabra original en la que las letras que no se han probado
       aparecen enmascaradas con un _.
    :rtype: str
    '''
    lista = []
    for letra in palabra:
        if letra in letras_probadas:
            lista.append(letra)
        else:
            lista.append("_")
    return str(lista)

def pedir_letra(letras_probadas):
    letra:str = input("Escribe una letra: ").lower()
    while not (len(letra)==1 and letra not in letras_probadas and letra.isalpha()):
        letra = input("Ese caracter no es válido, escribe otro: ").lower()
    return letra

def comprobar_letra(palabra_secreta:str, letra):
    conjunto = set(palabra_secreta)
    if letra in conjunto:
        return True
    else :
        return False

def mostrar_mensaje (acierto):
    if acierto:
        print("¡Bien hecho! Esa letra está en la palabra.")
    else:
        print("Lo siento, esa letra no está en la palabra.")

def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    for letra in palabra_secreta:
        if letra not in letras_probadas:
            return False
    return True