def buscar_libros_por_autor(autor_buscado):
    libros_encontrados = []

    # Abrir el archivo en modo de lectura
    try:
        with open("libros.txt", "r") as archivo:
            # Leer cada línea del archivo
            for linea in archivo:
                # Dividir la línea en nombre del libro y autor
                nombre_libro, autor = linea.strip().split(", ")
                
                # Verificar si el autor coincide con el autor buscado
                if autor.lower() == autor_buscado.lower():
                    libros_encontrados.append(nombre_libro)

        # Mostrar resultados
        if libros_encontrados:
            print(f"Libros de {autor_buscado}:")
            for libro in libros_encontrados:
                print(f"- {libro}")
        else:
            print(f"No se encontraron libros del autor '{autor_buscado}'.")
    except FileNotFoundError:
        print("El archivo libros.txt no se encontró.")

# Solicitar el nombre del autor al usuario y llamar a la función
autor_buscado = input("Ingrese el nombre del autor: ")
buscar_libros_por_autor(autor_buscado)
