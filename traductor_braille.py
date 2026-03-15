
"""
Traductor Español → Braille
Paul Mauricio Moreno Polanía
Iteraciones: 1-5 completas
"""

# Diccionario COMPLETO español a Braille Unicode
BRAILLE_DICT = {
    # Letras minúsculas A-Z
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
    
    # Español especial
    'ñ': '⠻', 'á': '⠷', 'é': '⠮', 'í': '⠌', 'ó': '⠬', 'ú': '⠾',
    'ü': '⠚⠥',
    
    # Números (prefijo ⠼ + letra)
    '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙',
    '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊',
    
    # Puntuación
    ' ': ' ', ',': '⠂', '.': '⠄', '?': '⠦', '!': '⠄', ';': '⠖',
    '-': '⠤', '(': '⠣', ')': '⠜', '"': '⠶'
}

def texto_a_braille(texto):
    """Convierte texto español a Braille"""
    resultado = []
    for char in texto.lower():
        if char in BRAILLE_DICT:
            resultado.append(BRAILLE_DICT[char])
        else:
            resultado.append(char)  # Mantiene caracteres no mapeados
    return ''.join(resultado)

def main():
    print("🔤 TRADUCTOR ESPAÑOL → BRAILLE")
    print("=" * 40)
    
    while True:
        # Input del usuario
        entrada = input("\nIngresa frase (o 'salir'): ").strip()
        
        if entrada.lower() in ['salir', 'exit', 'q']:
            print("¡Gracias por usar el traductor! 👋")
            break
        
        if not entrada:
            print("Por favor ingresa texto válido.")
            continue
        
        # Traducir
        braille = texto_a_braille(entrada)
        
        # Mostrar en pantalla
        print(f"\nEspañol: {entrada}")
        print(f"Braille: {braille}")
        print("-" * 40)
        
        # Guardar en archivo
        nombre_archivo = "salida_braille.txt"
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                f.write(f"TRADUCCIÓN BRAILLE - {entrada}\n")
                f.write(f"Braille: {braille}\n")
                f.write("=" * 40 + "\n")
            print(f"✅ Guardado en '{nombre_archivo}'")
        except Exception as e:
            print(f"Error guardando archivo: {e}")
    
    print("Fin del programa.")

if __name__ == "__main__":
    main()
# Tarea a Realizar: agregar funcion para traducir Braille a texto español (iteración 6)