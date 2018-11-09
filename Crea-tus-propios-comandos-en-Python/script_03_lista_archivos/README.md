# Descripción #
Toma los datos de cada archivo en PATH y los imprime en la salida estándar en formato de columnas de ancho fijo, si PATH no se proporciona entonces se usa el directorio actual.

## l.py, Ver 0.1 ##
Este script será similar al comando ls de Linux o Mac o al dir de Windows e imprimirá en la salida estándar la lista de archivos del directorio indicado por PATH, haremos 2 versiones, en la segunda versión la salida será en formato CSV usando la opción --to-csv.
Se incluyen las siguientes columnas:
- Nombre
- Extensión
- Tamaño

Ejecución:
```
python l-0.1.py --help

python l-0.1.py
```


## l.py, Ver 0.2##

Opciones:
`--tocsv` Imprime en la salida estándar la lista de archivos en formato CSV

Ejecución:
```
python l-0.2.py --help

python l-0.2.py --tocsv > salida.csv
```

## l.py, Ver 0.3##
En esta versión agregamos dos opciones al script, la primera `--to-html` para que imprima en la salida estándar la lista de archivos en formato HTML y la segunda (--to-xls) para que guarde la lista de archivos en un archivo en formato XLS.
`--to-xls` Guarda la lista de archivo en formato XLS en el archivo salida.xls
`--to-html` Guarda la lista de archivo en formato html en el archivo salida.html

Ejecución:
```
python l-0.3.py --help

python l-0.3.py --to-html > salida.html

python l-0.3.py --to-xls > salida.xls

```

