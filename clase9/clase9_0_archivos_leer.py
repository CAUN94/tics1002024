# En general en python muchas veces nos tocara trabajar con fuentes de datos que no necesariamentet esten en nuestro codigo, estas fuentes de datos pueden ser archivos, bases de datos, servicios web, etc.

# En esta caso usaremos archivos de texto (.txt) para leer y escribir informacion, ya que son de los más sencillos de usar.

# En este caso usaremos el archivo1.txt que contiene la siguiente informacion:

# Para abrir un archivo en python usamos la funcion open(), esta funcion recibe dos parametros, el primero es el nombre del archivo y el segundo es el modo en el que se va a abrir el archivo, los modos pueden ser: 'r' para leer, 'w' para escribir, 'a' para agregar, 'r+' para leer y escribir, 'w+' para leer y escribir, 'a+' para leer y escribir.

# Para leer un archivo usamos el metodo readline() que nos permite leer una linea del archivo, si se llama varias veces se iran leyendo las siguientes lineas.

# Cerremos el archivo

# Ahora si queremos separar la informacion de cada linea podemos usar el metodo split() que nos permite separar un string en una lista de strings, por defecto separa por espacios, pero se le puede pasar un parametro para que separe por otro caracter.

# Generalmente estos archivos contienen informacion separada por comas, en este caso la linea es "1,2,3,4,5,6,7,8,9,10\n" y queremos separarla por comas, pero antes debemos quitar el salto de linea que se genera al final de cada linea.
# Usaremos el comando strip para quitar el salto de linea


# Usamos el comando split para separar la linea en una lista de strings, en este caso se separa por ","

# Repetimos el proceso para las siguientes lineas


# Ahora el largo de la lista puede variar, por lo que si queremos acceder a un elemento en especifico debemos hacerlo por su indice


# Y ahora si queremos leer todo el archivo podemos usar un ciclo while

# Cerremos el archivo

