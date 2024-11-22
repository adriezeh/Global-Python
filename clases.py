import random

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
    
    
class Mutador:
    def __init__(self, base_nitrogenada, tipo_mutacion):
        self.base_nitrogenada = base_nitrogenada
        self.tipo_mutacion = tipo_mutacion

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_mutacion):
        pass 



class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, intensidad):
        super().__init__(base_nitrogenada, "Radiacion")
        self.intensidad = intensidad

    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_mutacion):
        try:
            matriz = [["A", "T", "C", "G"] for _ in range(5)] 
            if orientacion_de_mutacion == "H":
                for j in range(4):
                    matriz[posicion_inicial[0]][posicion_inicial[1] + j] = base_nitrogenada
            elif orientacion_de_mutacion == "V":
                for i in range(4):
                    matriz[posicion_inicial[0] + i][posicion_inicial[1]] = base_nitrogenada
            return matriz
        except Exception as e:
            print(f"Error: {e}")
            return None