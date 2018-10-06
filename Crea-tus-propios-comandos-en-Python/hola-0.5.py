import sys
def help():
    """Imprime la ayuda del script en la salida estándar
    """
    print("""
Sintaxis
hola.py [--help] tuNombre

Imprime en la salida estándar el saludo incluyendo tuNombre

Opciones:
--help Imprime en la salida estándar esta ayuda
    """)
    
def main(argv):
    """Función principal del script
    """
    if len(argv) < 2:
        help()
        sys.exit(0)
    if "--help" in argv[1]:
        help()
        sys.exit(0)
    elif "--" in argv[1]:
        print("La opción {} no existe".format(argv[1]))
        print()
        sys.exit(0)        
        
    print(("Hola {}!".format(argv[1])).upper())
if __name__ == "__main__":
    main(sys.argv)