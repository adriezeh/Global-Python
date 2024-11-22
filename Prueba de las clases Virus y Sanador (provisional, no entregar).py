# Este archivo solo fue creado por Lea para probar si clase virus y clase sanador funcionan correctamente
if __name__ == "__main__":
    matriz_adn = [
        "AGATCA",
        "GATTCA",
        "CAACAT",
        "GAGCTA",
        "ATTGCG",
        "CTGTTC"
    ]
    
    # Crear un objeto de Virus
    virus = Virus('T', [])
    
    # Crear un mutante en la diagonal
    matriz_mutada = virus.crear_mutante('T', (0, 0))
    print("Matriz mutada por el Virus:")
    for fila in matriz_mutada:
        print(fila)

    # Crear un objeto Sanador
    sanador = Sanador()
    
    # Sanar la matriz mutada
    matriz_sanada = sanador.sanar_mutantes(matriz_mutada)
    print("Matriz después de sanar:")
    for fila in matriz_sanada:
        print(fila)
