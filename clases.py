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
    
    class Virus(Mutador):
    def __init__(self, base_nitrogenada, energia_viral=100, tipo_virus='diagonal'):
        """
        Constructor de la clase Virus
        
        Args:
            base_nitrogenada (str): Base nitrogenada que se repetirá
            energia_viral (int, opcional): Nivel de energía del virus. Por defecto 100.
            tipo_virus (str, opcional): Tipo de virus. Por defecto 'diagonal'.
        """
        super().__init__()
        self.base_nitrogenada = base_nitrogenada
        self.energia_viral = energia_viral
        self.tipo_virus = tipo_virus
    
    def crear_mutante(self, base_nitrogenada, posicion_inicial, matriz):
        """
        Crea una mutación diagonal en la matriz de ADN
        
        Args:
            base_nitrogenada (str): Base nitrogenada a mutar
            posicion_inicial (tuple): Coordenadas de inicio de la mutación
            matriz (list): Matriz de ADN
        
        Returns:
            list: Matriz de ADN mutada
        """
        try:
            fila, columna = posicion_inicial
            
            # Verificar límites de la matriz para mutación diagonal
            if fila + 3 >= len(matriz) or columna + 3 >= len(matriz[0]):
                raise ValueError("Posición inicial no permite mutación diagonal completa")
            
            # Crear mutación diagonal
            for i in range(4):
                matriz[fila + i][columna + i] = base_nitrogenada
            
            return matriz
        
        except IndexError:
            print("Error: Posición fuera de los límites de la matriz")
            return matriz
        except ValueError as e:
            print(f"Error: {e}")
            return matriz

class Sanador:
    def __init__(self, tecnica_sanacion='regenerativa', probabilidad_exito=0.8):
        """
        Constructor de la clase Sanador
        
        Args:
            tecnica_sanacion (str, opcional): Técnica de sanación. Por defecto 'regenerativa'
            probabilidad_exito (float, opcional): Probabilidad de éxito de sanación. Por defecto 0.8
        """
        self.tecnica_sanacion = tecnica_sanacion
        self.probabilidad_exito = probabilidad_exito
    
    def sanar_mutantes(self, matriz, detector):
        """
        Sana mutaciones en la matriz de ADN generando una nueva matriz sin mutaciones
        
        Args:
            matriz (list): Matriz de ADN original
            detector (Detector): Instancia de la clase Detector para verificar mutaciones
        
        Returns:
            list: Nueva matriz de ADN sin mutaciones
        """
        # Verificar si hay mutaciones
        if detector.detectar_mutantes(matriz):
            # Generar nueva matriz
            bases = ['A', 'C', 'G', 'T']
            nueva_matriz = []
            
            # Crear matriz aleatoria hasta que no tenga mutaciones
            while True:
                nueva_matriz = [
                    [random.choice(bases) for _ in range(len(matriz[0]))] 
                    for _ in range(len(matriz))
                ]
                
                if not detector.detectar_mutantes(nueva_matriz):
                    break
            
            return nueva_matriz
        
        return matriz