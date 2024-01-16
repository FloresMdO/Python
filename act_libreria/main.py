import os
from datetime import datetime

def menu():
    print(" 1. Registro de nuevo libro")
    print(" 2. Prestamo de un libro")
    print(" 3. Devolucion de un libro")
    print(" 4. Consulta de Libro")
    print(" 5. Estadisticas")
    print(" 6. Salir\n")

def redistro_libros(biblioteca):
    print("\nRegistrar un nuevo libro\n")
    qty_libros = int(input("Cuantos libros deseas agregar? "))

    libro =  {
        'titulo': '',
        'autor': '',
        'fecha_publicacion': '',
        'libro_id': 0,
        'fecha_prestamo': '',
        'fecha_devolucion': '',
        'disponible': True,
    }

    for i in range(qty_libros):
        print("\nDatos del libro " + str(i+1) + "\n")

        # Solicitamos los datos del libro.
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        publication_date = int(input("Ano de publicacion del libro: "))
        libro_id = int(input("No. Identificacion del libro: "))

        # Creamos un diccionario con los datos del libro.
        libro = {
            "titulo": titulo,
            "autor": autor,
            "fecha_publicacion": publication_date,
            "libro_id": libro_id,
            "disponible": True,
        }

        # Añadimos el diccionario del libro al diccionario anidado.
        biblioteca[libro_id] = libro

    return biblioteca

def solicitar_prestamo(biblioteca):
    print("\nSolicitar prestamos de un libro\n")

    prestamo_lib = input("Ingresa el titulo del libro: ")

    for libro_id, libro_info in biblioteca.items():
        if libro_info['titulo'].lower() == prestamo_lib.lower():
            if libro_info['disponible']:
                opcion = input("\nEl libro esta disponible para prestamos, desea solicitar el prestamo? (S/n): ")
                if opcion.lower() == 's':
                    print("\nPara el prestamos del libro, ingresa los siguientes datos: \n")

                    fecha_prestamo = input("Ingresa la fecha del prestamo (YYYY-MM-DD): ")
                    fecha_prestamo = try_fecha(fecha_prestamo)

                    fecha_devolucion = input("Ingresa la fecha en la que devolveras el libro  (YYYY-MM-DD): ")
                    fecha_devolucion = try_fecha(fecha_devolucion)

                    libro_info.update({
                        'fecha_prestamo': fecha_prestamo,
                        'fecha_devolucion': fecha_devolucion,
                        'disponible': False
                    })
                else:
                    print("\nNos vemos luego")
            else:
                print(f"\nEl libro no está disponible. Se prestó el {libro_info['fecha_prestamo']} y se planea devolver el {libro_info['fecha_devolucion']}\n")
            return
    print("\nEl libro no existe en la biblioteca.")

def try_fecha(fecha_ingresada):
    try:
        fecha = datetime.strptime(fecha_ingresada, "%Y-%m-%d")
        return fecha
    except ValueError:
        print("Formato incorreco")
    

def devolver_libro(biblioteca):
    print("Devolaucion  de un libro\n")

    devolucion_lib = input("Libro a devolver: ")

    for libro_id, libro_info in biblioteca.items():
        if libro_info['titulo'].lower() == devolucion_lib.lower():
            if libro_info['disponible'] == False:
                print(f"\n+El libro e prestó el {libro_info['fecha_prestamo']} y se planea devolver el {libro_info['fecha_devolucion']}\n")

                devolver_lib = input("Desea devolver el libro? (S/n): ")

                if devolver_lib.lower() == 's':
                    fecha_entrega = datetime.now()
                    print(f"El libro {libro_info['titulo']} se entrego el {fecha_entrega}")

                    libro_info.update({
                        'fecha_prestamo': '',
                        'fecha_devolucion': fecha_entrega,
                        'disponible': True
                    })
                else:
                    print("Recuerde que una entrrega tardia puede proporcionar una multa.")
    

def consultar_libro(biblioteca):
    print("\nBuscador de libro\n")

    buscar_por = int(input("Buscar libros por:\n \n 1. Titulo\n 2. Autor\n 3. Ano de publicacion\n 4. Cancelar\n \nOpcion: "))
    filtro = ('Titulo' if buscar_por == 1 else 'Autor' if buscar_por == 2 else 'Ano de publicacion')

    if buscar_por in [1,2,3]:
        criterio = input("\nBuscar libro.\n \nIngresa el "+''.join(filtro)+" del Libro a consultar:")
        for libro_id, libro_info in biblioteca.items():
            if libro_info['titulo'].lower() == criterio if buscar_por == 1 else libro_info['autor'].lower() == criterio if buscar_por == 2 else str(libro_info['fecha_publicacion']) == criterio:
                imprimir_libros_consulta(libro_info)
                return
        print("\nEl libro no existe en la biblioteca.")
    else:
        print("Opción no válida.")


def imprimir_libros_consulta(libro_info):
        print(f"""
Titulo: {libro_info['titulo']}
Autor: {libro_info['autor']}
Ano de publicacion: {libro_info['fecha_publicacion']}
No. Identificacion: {libro_info['libro_id']}
""")

def estadisticas(biblioteca):
    libros_disponibles = 0
    libros_prestados = 0
    libros_atrasados = 0

    for libro_info in biblioteca.values():
        if libro_info['dosponible'] == True:
            libros_disponibles += 1
        else:
            libros_prestados += 1
            fecha_devolucion = datetime.strptime(libro_info['fecha_devolucion'], "%Y-%m-%d")
            fecha_actual = datetime.now()

            if fecha_devolucion > fecha_actual:
                libros_atrasados += 1

    print("Estadisticas de la biblioteca\n")
    print(f"""
Libros disponibles: {libros_disponibles}
Libros prestados: {libros_prestados}
Libros atrasados: {libros_atrasados}
""")

biblioteca = {}
opcion = 0
while(opcion != 5):
    print("\nBienvenido a la biblioteca, que deseahacer hoy?\n")
    menu(); 
    
    try: 
        opcion = int(input("Opcion: "))
    except ValueError:
        print("\nIngresa una opcion valida.")
        continue

    if opcion == 1:
        redistro_libros(biblioteca)
    elif opcion == 2:
        solicitar_prestamo(biblioteca)
    elif opcion == 3:
        devolver_libro(biblioteca)
    elif opcion == 4:
        consultar_libro(biblioteca)
    elif opcion == 5:
        estadisticas(biblioteca)
    else:
        break