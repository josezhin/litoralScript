#!/usr/bin/python3

#Información de los libros en forma de diccionarios
libro1 = {'nombre': 'Harry Potter y la piedra filosofal', 'codigo': 'HPJK1997', 'autor': 'J.K Rowling', 'año publicacion': 1997, 'cantidad': 200, 'precio': 25000, 'costo': 9000}
libro2 = {'nombre': 'Los Juegos del Hambre', 'codigo': 'JHSC2008', 'autor': 'Suzanne Collins', 'año publicacion': 2008, 'cantidad': 20, 'precio': 27000, 'costo': 12000}
libro3 = {'nombre': 'El Hobbit', 'codigo': 'EHJR1937', 'autor': 'J.R.R.Tolkien', 'año publicacion': 1937, 'cantidad': 100, 'precio': 35000, 'costo': 15000}
libro4 = {'nombre': 'Hamlet', 'codigo': 'HWS1589', 'autor': 'William Shakespeare', 'año publicacion': 1589, 'cantidad': 20, 'precio': 26000, 'costo': 13000}

#Lista con la información de los libros
libros = [libro1, libro2, libro3, libro4]

#Función que determina el libro con mayor ganancia
def mejor_opcion(libros):
    opcion = None
    ganancia_max = 0
    
    for libro in libros:
        demanda = libro['cantidad']
        precio = libro['precio']
        costo = libro['costo']
        ganancia = precio - costo
        
        if demanda >= 100 and ganancia > 14000:
            if demanda > 800:
                precio *= 1.1
            
            ganancia = precio - costo
            
            if ganancia > ganancia_max:
                opcion = libro
                ganancia_max = ganancia
    
    if opcion:
        return f"La mejor opción de libro es '{opcion['nombre']}' de {opcion['autor']}, con código {opcion['codigo']}, publicado en {opcion['año publicacion']} y precio de venta de ${precio:,.0f}."
    else:
        return "Ninguno de los libros es la mejor opción para ser vendido."
print(mejor_opcion(libros))
