# Ajedrez
Este proyecto implementa un sencillo juego de ajedrez en consola utilizando Python. El programa permite a los jugadores mover las piezas de ajedrez y guarda los tableros resultantes en un archivo de texto.
## Funciones
### get_coordinates(posicion)
Convierte una posición en formato de ajedrez (por ejemplo, "G2") a índices de fila y columna en el tablero.
### print_board(tablero)
Imprime el tablero en la consola, utilizando caracteres Unicode para simular las piezas de ajedrez. Además, guarda el tablero en un archivo de texto llamado "tablero.txt".
### save_board(tablero, nombre_archivo)
Guarda el tablero en un archivo de texto. Cada llamada agrega el tablero modificado al final del archivo.
### move_piece(tablero)
Permite al jugador mover una pieza. Solicita la posición de origen y destino, verifica la validez del movimiento y actualiza el tablero. Además, guarda cada movimiento en el archivo "tablero.txt".
## Uso
1. El tablero inicial se imprime en la consola y se guarda en el archivo "tablero.txt".
2. Se permite al jugador mover piezas mediante la función **'move_piece(tablero)'**.
3. Cada movimiento se imprime en la consola y se guarda en el archivo "tablero.txt".
4. El juego continuará solicitando movimientos hasta que el jugador decida terminar.
## Tablero Inicial
El tablero inicial se representa con caracteres Unicode para simular las piezas de ajedrez. Las letras de las columnas y los números de las filas se muestran en la parte inferior del tablero.
## Link al repositorio
https://github.com/AlvaroSantamariaAnton/Santamaria_Alvaro_Ajedrez.git