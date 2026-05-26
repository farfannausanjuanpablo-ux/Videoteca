peliculas = [
    ["Avatar", 2009, 9, "Ciencia ficción"],
    ["Titanic", 1997, 8, "Romance"],
    ["Avengers Endgame", 2019, 9, "Acción"],
    ["Joker", 2019, 8, "Drama"],
    ["Interstellar", 2014, 10, "Ciencia ficción"],
    ["Toy Story 4", 2019, 7, "Animación"],
    ["El Padrino", 1972, 10, "Crimen"]
]

def contar_titulos(calificacion_minima, año_minimo):
    contador = 0

    for pelicula in peliculas:
        año = pelicula[1]
        calificacion = pelicula[2]

        if calificacion >= calificacion_minima and año >= año_minimo:
            contador += 1

    return contador


def menu():
    print("🎬 VIDEOTECA DIGITAL")

    calificacion_minima = float(input("Ingresa calificación mínima (1-10): "))
    año_minimo = int(input("Ingresa año mínimo: "))

    resultado = contar_titulos(calificacion_minima, año_minimo)

    print("\n📊 RESULTADO")
    print("Títulos que cumplen:", resultado)


menu()