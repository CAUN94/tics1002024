# Paso 1: Leer el archivo notas.txt y convertirlo en una matriz
def leer_archivo_notas():
    archivo = open("notas.txt", "r")
    matriz_notas = []
    for i in range(100):
        linea = archivo.readline().strip()
        datos = linea.split(",")
        matriz_notas.append(datos)
    archivo.close()
    return matriz_notas

# Paso 2: Calcular la nota mayor
def calcular_nota_mayor(matriz_notas):
    nota_mayor = 7  # Iniciar con una nota superior a 7
    for i in range(len(matriz_notas)):
        for j in range(2, len(matriz_notas[i])):
            nota = float(matriz_notas[i][j])
            if nota != 1 and nota > nota_mayor:
                nota_mayor = nota
    return nota_mayor

# Paso 3: Calcular la nota menor
def calcular_nota_menor(matriz_notas):
    nota_menor = 0  # Iniciar con una nota superior a 0
    for i in range(len(matriz_notas)):
        for j in range(2, len(matriz_notas[i])):
            nota = float(matriz_notas[i][j])
            if nota != 1 and nota < nota_menor:
                nota_menor = nota
    return nota_menor

# Paso 4: Calcular el promedio de notas
def calcular_promedio_notas(matriz_notas):
    suma_notas = 0
    contador_notas = 0
    for i in range(len(matriz_notas)):
        for j in range(2, len(matriz_notas[i])):
            nota = float(matriz_notas[i][j])
            if nota != 1:
                suma_notas += nota
                contador_notas += 1
    promedio = suma_notas / contador_notas
    if contador_notas == 0:
        promedio = 0
    return promedio

# Paso 5: Identificar a los alumnos que aprobaron, fueron a examen y reprobaron
def categorizar_alumnos(matriz_notas):
    aprobados = []
    examen = []
    reprobados = []
    for i in range(len(matriz_notas)):
        suma_notas = 0
        contador_notas = 0
        for j in range(2, len(matriz_notas[i])):
            nota = float(matriz_notas[i][j])
            if nota != 1:
                suma_notas += nota
                contador_notas += 1
        promedio = suma_notas / contador_notas if contador_notas != 0 else 0
        if promedio >= 5.5:
            aprobados.append(matriz_notas[i])
        elif promedio >= 3 and promedio < 5.5:
            examen.append(matriz_notas[i])
        else:
            reprobados.append(matriz_notas[i])
    return aprobados, examen, reprobados

# Paso 6: Escribir los resultados en el archivo resumen.txt
def escribir_resumen(nota_mayor, nota_menor, promedio, aprobados, examen, reprobados):
    archivo = open("resumen.txt", "w")
    archivo.write(f"Nota Mayor: {nota_mayor}\n")
    archivo.write(f"Nota Menor: {nota_menor}\n")
    archivo.write(f"Promedio de Notas: {promedio}\n")
    archivo.write("Alumnos Aprobados:\n")
    for estudiante in aprobados:
        archivo.write(f"{','.join(estudiante)}\n")
    archivo.write("Alumnos en Examen:\n")
    for estudiante in examen:
        archivo.write(f"{','.join(estudiante)}\n")
    archivo.write("Alumnos Reprobados:\n")
    for estudiante in reprobados:
        archivo.write(f"{','.join(estudiante)}\n")
    archivo.close()

# Paso 7: Escribir los correos de los alumnos en archivos separados
def escribir_resumen(nota_mayor, nota_menor, promedio, aprobados, examen, reprobados):
    archivo = open("resumen.txt", "w")
    archivo.write("Nota Mayor: " + str(nota_mayor) + "\n")
    archivo.write("Nota Menor: " + str(nota_menor) + "\n")
    archivo.write("Promedio de Notas: " + str(promedio) + "\n")
    archivo.write("Alumnos Aprobados:\n")
    for estudiante in aprobados:
        for dato in estudiante:
            archivo.write(str(dato) + ",")
        archivo.write("\n")
    archivo.write("Alumnos en Examen:\n")
    for estudiante in examen:
        for dato in estudiante:
            archivo.write(str(dato) + ",")
        archivo.write("\n")
    archivo.write("Alumnos Reprobados:\n")
    for estudiante in reprobados:
        for dato in estudiante:
            archivo.write(str(dato) + ",")
        archivo.write("\n")
    archivo.close()

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
