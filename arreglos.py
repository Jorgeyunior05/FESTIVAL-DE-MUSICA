def agregar_canciones(nombres, artistas, duraciones, popularidades):
    try:
        n = int(input("¿Cuántas canciones deseas agregar? "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    for i in range(n):
        print(f"\nCanción {i+1}:")
        nombre = input("Nombre: ").strip()
        artista = input("Artista: ").strip()

        while True:
            try:
                duracion = float(input("Duración en minutos: "))
                if duracion <= 0:
                    print("Duración debe ser mayor que 0.")
                    continue
                break
            except ValueError:
                print("Por favor ingresa un número válido.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                else:
                    print("Popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Por favor ingresa un número válido.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)
    print(f"\nSe agregaron {n} canciones exitosamente.")


def mostrar_reportes(nombres, artistas, duraciones, popularidades):
    if not nombres:
        print("No hay canciones registradas aún.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    popularidad_promedio = sum(popularidades) / total_canciones

    indice_max = popularidades.index(max(popularidades))
    indice_min = popularidades.index(min(popularidades))

    print("\n--- Reporte de la Playlist ---")
    print(f"Número total de canciones: {total_canciones}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print(f"Canción más popular: '{nombres[indice_max]}' de {artistas[indice_max]} (Popularidad: {popularidades[indice_max]})")
    print(f"Canción menos popular: '{nombres[indice_min]}' de {artistas[indice_min]} (Popularidad: {popularidades[indice_min]})")
    print(f"Promedio de popularidad: {popularidad_promedio:.2f}")


def buscar_por_artista(nombres, artistas, duraciones, popularidades):
    artista_busqueda = input("Ingresa el nombre del artista a buscar: ").strip().lower()
    encontrados = [(nombres[i], artistas[i], duraciones[i], popularidades[i])
                  for i in range(len(nombres)) if artistas[i].lower() == artista_busqueda]

    if not encontrados:
        print(f"No se encontraron canciones del artista '{artista_busqueda}'.")
    else:
        print(f"\nCanciones de '{artista_busqueda}':")
        for nombre, artista, duracion, popularidad in encontrados:
            print(f"- {nombre} | Duración: {duracion} min | Popularidad: {popularidad}")


def buscar_por_rango_popularidad(nombres, artistas, duraciones, popularidades):
    try:
        min_pop = int(input("Popularidad mínima (1-100): "))
        max_pop = int(input("Popularidad máxima (1-100): "))
        if not (1 <= min_pop <= 100 and 1 <= max_pop <= 100 and min_pop <= max_pop):
            print("Rangos inválidos.")
            return
    except ValueError:
        print("Por favor ingresa números válidos para popularidad.")
        return

    encontrados = [(nombres[i], artistas[i], duraciones[i], popularidades[i])
                  for i in range(len(nombres))
                  if min_pop <= popularidades[i] <= max_pop]

    if not encontrados:
        print(f"No se encontraron canciones con popularidad entre {min_pop} y {max_pop}.")
    else:
        print(f"\nCanciones con popularidad entre {min_pop} y {max_pop}:")
        for nombre, artista, duracion, popularidad in encontrados:
            print(f"- {nombre} de {artista} | Duración: {duracion} min | Popularidad: {popularidad}")


def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    if not nombres:
        print("No hay canciones registradas aún.")
        return

    promedio = sum(popularidades) / len(popularidades)
    recomendadas = [(nombres[i], artistas[i], duraciones[i], popularidades[i])
                    for i in range(len(nombres)) if popularidades[i] > promedio]

    if not recomendadas:
        print("No hay canciones con popularidad superior al promedio.")
    else:
        print(f"\nPlaylist recomendada (Popularidad > {promedio:.2f}):")
        for nombre, artista, duracion, popularidad in recomendadas:
            print(f"- {nombre} de {artista} | Duración: {duracion} min | Popularidad: {popularidad}")


def menu():
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []

    while True:
        print("\n--- Menú Festival Playlist ---")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "2":
            mostrar_reportes(nombres, artistas, duraciones, popularidades)
        elif opcion == "3":
            print("\nBuscar por:")
            print("a) Artista")
            print("b) Rango de popularidad")
            sub_op = input("Elige una opción (a/b): ").strip().lower()
            if sub_op == "a":
                buscar_por_artista(nombres, artistas, duraciones, popularidades)
            elif sub_op == "b":
                buscar_por_rango_popularidad(nombres, artistas, duraciones, popularidades)
            else:
                print("Opción inválida.")
        elif opcion == "4":
            playlist_recomendada(nombres, artistas, duraciones, popularidades)
        elif opcion == "5":
            print("¡Gracias por usar Festival Playlist! Hasta luego.")
            break
        else:
            print("Opción inválida, por favor intenta de nuevo.")


if __name__ == "__main__":
    menu()
