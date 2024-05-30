# Enunciado del Ejercicio:

"""
El objetivo de este ejercicio es procesar un archivo de notas de estudiantes, realizar diversos cálculos y generar un resumen de los resultados en un nuevo archivo.

El archivo notas.txt contiene información de notas de estudiantes en el siguiente formato: "nombre estudiante","Mail alumno", "nota prueba 1","nota prueba 2","nota prueba 3". 
Cada línea del archivo representa un estudiante con su respectivo nombre, correo electrónico y tres notas de pruebas.

El programa debe realizar los siguientes pasos utilizando funciones definidas (def):

1. Leer el archivo notas.txt y convertirlo en una matriz de datos.

2. Calcular la nota mayor entre todas las notas de los estudiantes.

3. Calcular la nota menor entre todas las notas de los estudiantes (las notas 1 asuma que son un no asistio y no se consideran).

4. Calcular el promedio de notas considerando únicamente las notas válidas (distintas de 1).

5. Identificar a los alumnos que aprobaron (promedio mayor o igual a 5.5), los que deben rendir examen (promedio entre 3 y 5.4) y los que reprobaron (promedio menor a 3).

6. Escribir un resumen de los resultados en un nuevo archivo resumen.txt, que incluya la nota mayor, la nota menor, el promedio de notas, la lista de alumnos aprobados, la lista de alumnos que deben rendir examen y la lista de alumnos reprobados.

7. Escribir los correos de los alumnos aprobados, los que deben rendir examen y los reprobados en archivos separados llamados correos_aprobados.txt, correos_examen.txt y correos_reprobados.txt respectivamente.


"""


# Paso 1: Leer el archivo notas.txt y convertirlo en una matriz
def leer_archivo_notas():
    pass
# Paso 2: Calcular la nota mayor
def calcular_nota_mayor(matriz_notas):
    pass

# Paso 3: Calcular la nota menor
def calcular_nota_menor(matriz_notas):
    pass
# Paso 4: Calcular el promedio de notas
def calcular_promedio_notas(matriz_notas):
    pass
# Paso 5: Identificar a los alumnos que aprobaron, fueron a examen y reprobaron
def categorizar_alumnos(matriz_notas):
    pass

# Paso 6: Escribir los resultados en el archivo resumen.txt
def escribir_resumen(nota_mayor, nota_menor, promedio, aprobados, examen, reprobados):
    pass

# Paso 7: Escribir los correos de los alumnos en archivos separados
def escribir_correos(aprobados, examen, reprobados):
    pass

# Paso 8: Definir función principal para ejecutar el análisis de notas.
def ejecutar():
    # Paso 1: Leer el archivo notas.txt y convertirlo en una matriz
    matriz_notas = leer_archivo_notas()

    # Paso 2: Calcular la nota mayor
    nota_mayor = calcular_nota_mayor(matriz_notas)

    # Paso 3: Calcular la nota menor
    nota_menor = calcular_nota_menor(matriz_notas)

    # Paso 4: Calcular el promedio de notas
    promedio = calcular_promedio_notas(matriz_notas)

    # Paso 5: Identificar a los alumnos que aprobaron, fueron a examen y reprobaron
    aprobados, examen, reprobados = categorizar_alumnos(matriz_notas)

    # Paso 6: Escribir los resultados en el archivo resumen.txt
    escribir_resumen(nota_mayor, nota_menor, promedio, aprobados, examen, reprobados)

    # Paso 7: Escribir los correos de los alumnos en archivos separados
    escribir_correos(aprobados, examen, reprobados)

# Llamar a la función principal para ejecutar el análisis
ejecutar()
