from traductor_braille import BRAILLE_DICT

def inversor_braile_español(diccionario:dict)->dict:
    """
    convierte el orden calve valor del diccionario.
    en este caso cambia el braile a una llave y su igual en español a un valor
    """
    return {v:k for k,v in BRAILLE_DICT.items()}

def traductor_braile_español(text:str):
    """
    traductor de español a braile
    """
    if not text: return ""

    resultado =""
    es_numeroco = "⠼"
    diccionario_español = inversor_braile_español(BRAILLE_DICT)
    i=0
    while i < len(text):
        char = text[i]
        if char == es_numeroco and (i+1) < len(text): 
            numer_char = text[i]+text[i+1]
            if numer_char in diccionario_español:
                resultado += diccionario_español[numer_char]
                i+=2
        elif char in diccionario_español:
            resultado += diccionario_español[char]
            i+=1
        else:
            resultado += char
            i+=1
        
    print(text, resultado)
    return resultado


if __name__ == "__main__":
    texto = "⠉⠁⠍⠊⠇⠕@⠼⠁⠼⠊⠼⠓⠼⠊⠼⠃⠼⠋"
    traductor_braile_español(texto)


