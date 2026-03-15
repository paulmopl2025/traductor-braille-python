from traductor_braille import BRAILLE_DICT,texto_a_braille

def inversor_braile_español(diccionario:dict)->dict:
    """
    convierte el orden calve valor del diccionario.
    en este caso cambia el braile a una llave y su igual en español a un valor
    """
    return {v:k for k,v in diccionario.items()}

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
                continue
        elif char in diccionario_español:
            resultado += diccionario_español[char]
        else:
            resultado += char
        i+=1   
    return resultado

def guardar_archivo(path:str, original:str,traducido:str)->None:
    with open(path, "w") as archivo:
        archivo.write("--- REPORTE DE TRADUCCIÓN ---\n")
        archivo.write(f"ENTRADA:\n {original}\n")
        archivo.write(f"SALIDA:\n  {traducido}\n")
    print(f"el Archivo {path}.txt fue guardado correctamente.")

def menu():
    opciones = {
            1:texto_a_braille,
            2:traductor_braile_español,
        }

    while True:
        print("\n--- Menú del Traductor ---")
        print("1. Traducir de Español a Braille")
        print("2. Traducir de Braille a Español")
        print("3. Salir")
        try:
            opcion = int(input("Ingresa la opcion que desees ejecutar (1,2,3)"))
        except ValueError:
            print(f" la {opcion} no es un numero, debe ser un numero entre 1 a 3, intentalo nuevamente.")
            continue
        if opcion == 3:
            print("estas saliendo de la aplicacion de traduccion")
            break
        if opcion in opciones:
            texto = input("Ingresa el texto que deseas traducir: ")  
            resultado = opciones[opcion](texto)

            print(f"El texto que ingresaste fue: {texto}")
            print(f"la traduccion fue: {resultado}")
            guardar = input("Deseas Guardar el archivo: Si/No")
            if guardar.lower() == "si":
                nombre = input("Ingresa el nombre que quieres que tenga el archovo: ")
                guardar_archivo(nombre, texto , resultado)
        else: 
            print("Opcion no valida, intentalo nuevamente.")

if __name__ == "__main__":
    texto = "⠉⠁⠍⠊⠇⠕@⠼⠁⠼⠊⠼⠓⠼⠊⠼⠃⠼⠋"
    menu()


