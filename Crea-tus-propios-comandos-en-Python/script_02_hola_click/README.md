# $ click_ `Command Line Interface Creation Kit` #

## ¿Qué es un Click? ##
Command Line Interface Creation Kit

## Instalando el módulo click con: ##
`$ pip install click`

## ¿Por qué Click? ##

    Toltalmente anidable y componible
    Generación de páginas de ayuda
    "Lazy loading" de comandos en tiempo de ejecución
    Soporte para las convenciones de UNIX
    Carga de variables de entorno de serie
    Soporte para Python 2 y 3
    Gestión de descriptores de ficheros de serie
    Muchos, muchos helpers


## ¿Y por qué no Argparse? ##

    Click está basado en optparse
    Hace demasiada "magia" para saber que es un argumento o un parámetro
    Dificulta el anidamiento de comandos

## Añadiendo parámetros, resultado ##
```
$ surprise --help
Usage: surprise [OPTIONS] NAME

Options:
  --count-down INTEGER  suprise countdown
  --help                Show this message and exit.

$ surprise --count-down 3 roberto
3...
2...
1...


Supriseeeeee!!!! roberto

```


##  Parámetros ##
Click soporta dos clases de parámetros: options y arguments

    Arguments
        mi_comando NOMBRE
        Usar para nombres, ficheros, etc.
    Options
        mi_comando --help
        Totalmente documentados
        Si falta el dato, te lo pide
        Precarga por variables de entorno


### Tipos de datos ###
    str / click.STRING
    int / click.INT
    float / click.FLOAT
    bool / click.BOOL
    click.UUID, click.File, click.Path, click.Choice, click.IntRange
    Tipos custom, muy faciles de implementar!


# Scripts #
Realizamos 2 versiones, donde veremos desde com imprimir información a la salida estándar, hasta como leer los argumentos de la linea de comandos y agregar opciones como la famosa `--help` utilizando `click`.

## holaclick.py tuNombre, Ver 0.1 ##


## holaclick.py tuNombre, Ver 0.2 ##
Agregar la opción:
`--repetir N`, donde N es el número de veces que se repite el mensaje con tuNombre.

## Referencias: ##
http://click.palletsprojects.com/en/7.x/
Presentación: `Haciendo comandos con Click!` autor: roberto.majadas  http://telemaco.github.io/python-click
