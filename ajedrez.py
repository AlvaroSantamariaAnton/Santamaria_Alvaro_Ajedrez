def get_coordinates(posicion):
    # Convierte la posición en formato de ajedrez a índices de fila y columna
    columna = ord(posicion[0].upper()) - ord("A") + 1  # Convierte la letra a índice de columna
    fila = 8 - int(posicion[1])  # Obtiene el índice de fila
    return fila, columna


def print_board(tablero):
    # Función para imprimir el tablero

    print()
    for fila in tablero:
        # Imprime cada elemento del tablero, utilizando un espacio en blanco en lugar de puntos
        print("\t".join(elemento if elemento != "." else " " for elemento in fila))
    print()


def save_board(tablero, nombre_archivo):
    # Función para guardar el tablero en un fichero

    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        # Agrega el tablero modificado al final del archivo
        for fila in tablero[:-1]:
            archivo.write("\t".join(str(elemento) for elemento in fila[1:]) + "\n")
        archivo.write("\n" + "\n")  # Agrega dos líneas en blanco para separar tableros


def move_piece(tablero):
    # Función para mover una pieza del tablero

    while True:
        mover = input("¿Quieres mover una pieza? (si/no): ").lower()

        if mover == "no":
            quit()
        elif mover == "si":
            break
        else:
            print("Por favor, ingresa 'si' para mover una pieza o 'no' para terminar.")
        
    while True:
        posicion_origen = input("Ingresa la posición de la pieza que quieres mover (por ejemplo, G2): ")
        posicion_destino = input("Ingresa la posición a la que quieres mover la pieza (por ejemplo, G3): ")

        fila_origen, columna_origen = get_coordinates(posicion_origen)
        fila_destino, columna_destino = get_coordinates(posicion_destino)

        # Verifica si las coordenadas están dentro del rango del tablero
        if 0 <= fila_origen < 8 and 0 <= columna_origen < 8 and 0 <= fila_destino < 8 and 0 <= columna_destino < 8:
            # Verifica si la pieza seleccionada pertenece al jugador
            if tablero[fila_origen][columna_origen] != " ":
                # Verifica si la casilla de destino está vacía
                if tablero[fila_destino][columna_destino] == " ":
                    # Realiza el movimiento
                    tablero[fila_destino][columna_destino] = tablero[fila_origen][columna_origen]
                    tablero[fila_origen][columna_origen] = " "
                    print_board(tablero)
                    # Guardar el tablero actualizado en el archivo después de cada movimiento
                    save_board(tablero, nombre_archivo)
                else:
                    print("La casilla de destino no está vacía. Elige otra posición.")
            else:
                print("La posición de origen no contiene una pieza tuya.")
        else:
            print("Coordenadas fuera de rango. Inténtalo de nuevo.")

        while True:
            seguir_moviendo = input("¿Quieres realizar otro movimiento? (si/no): ").lower()

            if seguir_moviendo == "no":
                quit()
            elif seguir_moviendo == "si":
                break
            else:
                print("Por favor, ingresa 'si' para mover una pieza o 'no' para terminar.")


if __name__ == "__main__":
    # Tablero inicial con caracteres Unicode para simular piezas de ajedrez
    tablero_inicial = [
        ['8', '♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
        ['7', '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['2', '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
        ['1', '♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['\n' ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    ]

    # Imprimir el tablero
    print_board(tablero_inicial)

    # Guardar el tablero inicial en un archivo
    nombre_archivo = "tablero.txt"
    save_board(tablero_inicial, nombre_archivo)

    # Permitir al jugador mover piezas
    move_piece(tablero_inicial)