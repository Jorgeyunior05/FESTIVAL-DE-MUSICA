class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, y represento el género {self.genero}.")

    def actuar(self):
        # Este método será sobrescrito en las subclases
        pass

    def despedirse(self):
        print(f"Gracias a todos, ¡hasta la próxima!")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"🎶 {self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"🎧 El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"🎸 La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


def iniciar_festival(lista_artistas):
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("🎆 Fin de la actuación 🎆\n")


def main():
    lista_artistas = []
    cantidad = int(input("¿Cuántos artistas se presentarán? "))

    for i in range(cantidad):
        print(f"\n--- Artista {i + 1} ---")
        tipo = input("Tipo de artista (Cantante, DJ o Banda): ").strip().lower()
        nombre = input("Nombre: ").strip()
        genero = input("Género musical: ").strip()
        popularidad = int(input("Popularidad (1-100): "))

        if tipo == "cantante":
            cancion = input("Canción más popular: ").strip()
            artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "dj":
            estilo = input("Estilo: ").strip()
            artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
        else:
            print("Tipo de artista no reconocido, se usará artista genérico.")
            artista = Artista(nombre, genero, popularidad)

        lista_artistas.append(artista)

    print("\n=== Comienza el Festival ===\n")
    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main()
