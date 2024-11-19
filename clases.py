import random

# Clase Detector
class Detector:
    def __init__(self):
        pass

    def detectar_mutantes(self, matriz_adn):
        """Detecta si hay una secuencia de bases nitrogenadas que se repiten 4 veces consecutivas."""
        for i in range(len(matriz_adn)):
            for j in range(len(matriz_adn[i])):
                if self.detectar_horizontal(matriz_adn, i, j) or self.detectar_vertical(matriz_adn, i, j) or self.detectar_diagonal(matriz_adn, i, j):
                    return True
        return False

    def detectar_horizontal(self, matriz_adn, i, j):
        """Detecta una mutación horizontal (4 bases consecutivas en la misma fila)."""
        if j <= len(matriz_adn[i]) - 4:
            secuencia = matriz_adn[i][j:j+4]
            if len(set(secuencia)) == 1:  # Las bases deben ser iguales
                return True
        return False

    def detectar_vertical(self, matriz_adn, i, j):
        """Detecta una mutación vertical (4 bases consecutivas en la misma columna)."""
        if i <= len(matriz_adn) - 4:
            secuencia = [matriz_adn[i+k][j] for k in range(4)]
            if len(set(secuencia)) == 1:
                return True
        return False

    def detectar_diagonal(self, matriz_adn, i, j):
        """Detecta una mutación diagonal (4 bases consecutivas en una diagonal)."""
        if i <= len(matriz_adn) - 4 and j <= len(matriz_adn[i]) - 4:
            secuencia = [matriz_adn[i+k][j+k] for k in range(4)]
            if len(set(secuencia)) == 1:
                return True
        return False