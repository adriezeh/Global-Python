import random


class Detector:
    def __init__(self, matriz: list[str]):
        self.matriz = matriz

    def detectar_mutantes(self) -> bool:
        """Detecta si hay mutaciones en la matriz"""
        if self.detectar_mutante_horizontal() or self.detectar_mutante_vertical() or self.detectar_mutante_diagonal():
            return True
        return False

    def detectar_mutante_horizontal(self) -> bool:
        """Detecta mutaciones horizontales (4 bases iguales seguidas en una fila)."""
        for fila in self.matriz:
            if 'TTTT' in fila or 'CCCC' in fila or 'AAAA' in fila or 'GGGG' in fila:
                return True
        return False

    def detectar_mutante_vertical(self) -> bool:
        """Detecta mutaciones verticales (4 bases iguales seguidas en una columna)"""
        for c in range(6):
            columna = ''.join([self.matriz[f][c] for f in range(6)])
            if 'TTTT' in columna or 'CCCC' in columna or 'AAAA' in columna or 'GGGG' in columna:
                return True
        return False

    def detectar_mutante_diagonal(self) -> bool:
        """Detecta mutaciones diagonales (4 bases iguales en una diagonal)"""
        for i in range(3):  # Comienza en fila y columna donde las diagonales caben
            for j in range(3):
                diagonal1 = ''.join([self.matriz[i+k][j+k] for k in range(4)])
                diagonal2 = ''.join([self.matriz[i+k][j+3-k] for k in range(4)])
                if 'TTTT' in diagonal1 or 'CCCC' in diagonal1 or 'AAAA' in diagonal1 or 'GGGG' in diagonal1:
                    return True
                if 'TTTT' in diagonal2 or 'CCCC' in diagonal2 or 'AAAA' in diagonal2 or 'GGGG' in diagonal2:
                    return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada: str, tipo_mutacion: str, posicion_inicial: tuple[int, int]):
        self.base_nitrogenada = base_nitrogenada
        self.tipo_mutacion = tipo_mutacion
        self.posicion_inicial = posicion_inicial

    def crear_mutante(self, matriz_usuario: list[str]) -> list[str]:
        """Método que muta la matriz proporcionada"""
        pass


class Radiacion(Mutador):
    def __init__(self, base_nitrogenada: str, tipo_mutacion: str, posicion_inicial: tuple[int, int]):
        super().__init__(base_nitrogenada, tipo_mutacion, posicion_inicial)

    def crear_mutante(self, matriz_usuario: list[str]) -> list[str]:
        matriz = matriz_usuario[:]  # Copia la matriz para no modificar la original
        if self.tipo_mutacion == "H":
            self._mutar_horizontal(matriz)
        elif self.tipo_mutacion == "V":
            self._mutar_vertical(matriz)
        return matriz

    def _mutar_horizontal(self, matriz: list[str]) -> None:
        """Realiza la mutación horizontal en la posición dada."""
        fila = list(matriz[self.posicion_inicial[0]])
        if self.posicion_inicial[1] + 3 >= 6:
            raise ValueError("La posición inicial no permite una mutación horizontal válida.")
        for i in range(4):
            fila[self.posicion_inicial[1] + i] = self.base_nitrogenada
        matriz[self.posicion_inicial[0]] = "".join(fila)

    def _mutar_vertical(self, matriz: list[str]) -> None:
        """Realiza la mutación vertical en la posición dada."""
        if self.posicion_inicial[0] + 3 >= 6:
            raise ValueError("La posición inicial no permite una mutación vertical válida.")
        for i in range(4):
            fila = list(matriz[self.posicion_inicial[0] + i])
            fila[self.posicion_inicial[1]] = self.base_nitrogenada
            matriz[self.posicion_inicial[0] + i] = "".join(fila)


class Virus(Mutador):
    def __init__(self, base_nitrogenada: str, tipo_mutacion: str, posicion_inicial: tuple[int, int]):
        super().__init__(base_nitrogenada, tipo_mutacion, posicion_inicial)

    def crear_mutante(self, matriz_usuario: list[str]) -> list[str]:
        matriz = matriz_usuario[:]  # Copia la matriz para no modificar la original
        self._mutar_diagonal(matriz)
        return matriz

    def _mutar_diagonal(self, matriz: list[str]) -> None:
        """Realiza la mutación diagonal en la posición dada."""
        if self.posicion_inicial[0] + 3 >= 6 or self.posicion_inicial[1] + 3 >= 6:
            raise ValueError("La posición inicial no permite una mutación diagonal válida.")
        for i in range(4):
            fila = list(matriz[self.posicion_inicial[0] + i])
            fila[self.posicion_inicial[1] + i] = self.base_nitrogenada
            matriz[self.posicion_inicial[0] + i] = "".join(fila)


class Sanador:
    def __init__(self, matriz_adn):
        self.matriz_adn = matriz_adn

    def sanar_mutantes(self):
        detector = Detector(self.matriz_adn)
        if detector.detectar_mutantes():
            print("Mutación detectada. Generando ADN sano...")
            return self.generar_adn_sano(len(self.matriz_adn), len(self.matriz_adn[0]))
        return self.matriz_adn

    def generar_adn_sano(self, filas, columnas):
        bases = ['A', 'T', 'C', 'G']
        return [[random.choice(bases) for _ in range(columnas)] for _ in range(filas)]