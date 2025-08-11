"""
    Autor: David Andrés Gómez Castro
    Fecha: 04 agosto 2025
    Descripción: Ejercicio 4 codigo morse
    
"""

MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-'
}


def texto_a_morse(texto):
    texto = texto.upper()  # Convertir a mayúsculas
    morse = []
    for char in texto:
        if char != ' ':
            morse.append(MORSE_CODE_DICT.get(char, ''))  # Convertir letra a Morse
        else:
            morse.append('/')  # Separar palabras con '/'
    return ' '.join(morse)

def morse_a_texto(morse):
    morse_inverso = {v: k for k, v in MORSE_CODE_DICT.items()}  # Diccionario inverso
    texto = []
    palabras = morse.split(' / ')  # Separar las palabras
    for palabra in palabras:
        letras = palabra.split()  # Separar las letras
        palabra_texto = ''.join([morse_inverso.get(letra, '') for letra in letras])
        texto.append(palabra_texto)
    return ' '.join(texto)

# Probar conversión de texto a Morse
texto = input("Digite la frase o palabra: ")
morse = texto_a_morse(texto)
print(f"Texto: {texto}")
print(f"Código Morse: {morse}")

# Probar conversión de Morse a texto
texto_recuperado = morse_a_texto(morse)
print(f"Texto recuperado: {texto_recuperado}")
