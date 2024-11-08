import csv

def actualizar_copias(nombre_libro, nuevas_copias):
    inventario_actualizado = []
    libro_encontrado = False

    # Leer el archivo y buscar el libro
    try:
        with open("inventario.csv", mode="r") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)  # Leer el encabezado
            inventario_actualizado.append(encabezado)

            for fila in lector:
                # Si el libro coincide, actualizar las copias
                if fila[0].lower() == nombre_libro.lower():
                    fila[1] = str(nuevas_copias)
                    libro_encontrado = True
                inventario_actualizado.append(fila)

        # Mostrar mensaje si el libro no se encuentra
        if not libro_encontrado:
            print(f"No se encontró el libro '{nombre_libro}' en el inventario.")
            return

        # Reescribir el archivo con los cambios
        with open("inventario.csv", mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(inventario_actualizado)
            print(f"Inventario actualizado exitosamente para el libro '{nombre_libro}'.")

    except FileNotFoundError:
        print("El archivo inventario.csv no se encontró.")

# Solicitar datos al usuario y llamar a la función
nombre_libro = input("Ingrese el nombre del libro: ")
nuevas_copias = input("Ingrese la nueva cantidad de copias: ")
if nuevas_copias.isdigit():
    actualizar_copias(nombre_libro, int(nuevas_copias))
else:
    print("Por favor, ingrese un número válido para la cantidad de copias.")
