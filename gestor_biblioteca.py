        # ============================
# FUNCIONES PRINCIPALES
# ============================

def agregar_libro(libros, titulo, autor, cantidad):
    for libro in libros:
        if libro["titulo"] == titulo and libro["autor"] == autor:
            libro["disponibles"] += cantidad
            print(f"Se han añadido {cantidad} ejemplares de '{titulo}'. Ahora hay {libro['disponibles']} disponibles.")
            return
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "disponibles": cantidad,
        "prestamos": 0
    }
    libros.append(nuevo_libro)
    print(f"Se ha añadido el libro '{titulo}' de {autor} con {cantidad} ejemplares.")

def prestar_libro(libros, historial_usuarios, usuario, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            if libro["disponibles"] > 0:
                libro["disponibles"] -= 1
                libro["prestamos"] += 1
                if usuario not in historial_usuarios:
                    historial_usuarios[usuario] = []
                historial_usuarios[usuario].append(titulo)
                print(f"Libro '{titulo}' prestado a {usuario}. Quedan {libro['disponibles']} disponibles.")
                recomendar_libro(libros, historial_usuarios, usuario)
                return
            else:
                print(f"No hay ejemplares disponibles de '{titulo}'.")
                return
    print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def devolver_libro(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            libro["disponibles"] += 1
            print(f"Libro '{titulo}' devuelto. Ahora hay {libro['disponibles']} disponibles.")
            return
    print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def consultar_disponibilidad(libros, titulo):
    for libro in libros:
        if libro["titulo"] == titulo:
            if libro["disponibles"] > 0:
                print(f"El libro '{titulo}' está disponible ({libro['disponibles']} ejemplares).")
            else:
                print(f"El libro '{titulo}' no está disponible en este momento.")
            return
    print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def recomendar_libro(libros, historial_usuarios, usuario):
    if usuario not in historial_usuarios or not historial_usuarios[usuario]:
        print(f"No hay historial de lectura para {usuario}, no se puede hacer una recomendación.")
        return

    autor_lecturas = {}
    for titulo_leido in historial_usuarios[usuario]:
        for libro in libros:
            if libro["titulo"] == titulo_leido:
                autor = libro["autor"]
                autor_lecturas[autor] = autor_lecturas.get(autor, 0) + 1

    autor_favorito = max(autor_lecturas, key=autor_lecturas.get)

    leidos = set(historial_usuarios[usuario])
    recomendaciones = [
        libro["titulo"]
        for libro in libros
        if libro["autor"] == autor_favorito and libro["titulo"] not in leidos and libro["disponibles"] > 0
    ]

    if recomendaciones:
        print(f"Recomendación para {usuario}: Podrías leer '{recomendaciones[0]}' de {autor_favorito}.")
    else:
        print(f"No hay más libros disponibles para recomendar de {autor_favorito}.")

# ============================
# DATOS DE EJEMPLO Y PRUEBAS
# ============================

libros = []
historial_usuarios = {}

# Agregar libros
agregar_libro(libros, "1984", "George Orwell", 3)
agregar_libro(libros, "Rebelión en la granja", "George Orwell", 2)
agregar_libro(libros, "Fahrenheit 451", "Ray Bradbury", 1)
agregar_libro(libros, "Crónicas marcianas", "Ray Bradbury", 2)

print("\n--- Préstamos ---")
prestar_libro(libros, historial_usuarios, "ana", "1984")
prestar_libro(libros, historial_usuarios, "ana", "Fahrenheit 451")
prestar_libro(libros, historial_usuarios, "ana", "Rebelión en la granja")

print("\n--- Devolución ---")
devolver_libro(libros, "1984")

print("\n--- Consultar Disponibilidad ---")
consultar_disponibilidad(libros, "1984")
consultar_disponibilidad(libros, "Fahrenheit 451")

print("\n--- Historial y Recomendaciones ---")
prestar_libro(libros, historial_usuarios, "ana", "Crónicas marcianas")
