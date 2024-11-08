def mostrar_prestamos():
    prestamos = []

    # Leer el archivo y cargar los préstamos en una lista
    try:
        with open("prestamos.txt", "r") as archivo:
            prestamos = [linea.strip() for linea in archivo.readlines()]

        # Mostrar los préstamos con numeración
        if prestamos:
            print("Préstamos actuales:")
            for i, prestamo in enumerate(prestamos, start=1):
                print(f"{i}. {prestamo}")
        else:
            print("No hay registros de préstamos.")
        return prestamos
    except FileNotFoundError:
        print("El archivo prestamos.txt no se encontró.")
        return None

def eliminar_prestamo():
    prestamos = mostrar_prestamos()
    
    if prestamos:
        # Solicitar al usuario el número del préstamo a eliminar
        try:
            numero_eliminar = int(input("Ingrese el número del préstamo que desea eliminar: "))
            
            # Validar si el número es válido
            if 1 <= numero_eliminar <= len(prestamos):
                prestamos.pop(numero_eliminar - 1)  # Eliminar el préstamo seleccionado

                # Reescribir el archivo con los préstamos actualizados
                with open("prestamos.txt", "w") as archivo:
                    for prestamo in prestamos:
                        archivo.write(prestamo + "\n")
                
                print("Préstamo eliminado exitosamente.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("No hay préstamos para eliminar.")

# Llamar a la función para iniciar el proceso de eliminación
eliminar_prestamo()
