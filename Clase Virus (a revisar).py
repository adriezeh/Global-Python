class Virus(Mutador):
    def __init__(self, base_nitrogenada, otros_atributos):
        super().__init__(base_nitrogenada, otros_atributos)

    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        """
        Crea una mutación diagonal a partir de la posición inicial.
        
        :param base_nitrogenada: la base que se va a repetir (por ejemplo, 'T')
        :param posicion_inicial: la posición de inicio de la mutación (tupla: fila, columna)
        :return: matriz de ADN con la mutación diagonal
        """
        try:
            fila, columna = posicion_inicial
            # Verificar si la mutación cabe dentro de la matriz
            if fila + 3 >= 6 or columna + 3 >= 6:
                raise ValueError("La mutación no cabe en la matriz a partir de la posición inicial.")

            # Crear una copia de la matriz original para no modificar la original
            matriz_mutada = [list(fila) for fila in matriz_adn]

            # Realizar la mutación diagonal
            for i in range(4):
                matriz_mutada[fila + i][columna + i] = base_nitrogenada

            # Convertir las filas de nuevo a strings
            matriz_mutada = ["".join(fila) for fila in matriz_mutada]
            return matriz_mutada

        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return matriz_adn  # Retornar la matriz original si ocurre un error
