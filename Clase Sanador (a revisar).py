import random

class Sanador:
    def __init__(self, atributos=None):
        # Aquí puedes agregar otros atributos si es necesario
        pass

    def generar_adn_aleatorio(self):
        """
        Genera una nueva matriz de ADN aleatoria de 6x6 sin mutaciones.
        
        :return: Una nueva matriz de ADN aleatoria
        """
        bases = ['A', 'T', 'C', 'G']
        matriz_aleatoria = []
        for _ in range(6):
            fila = ''.join(random.choice(bases) for _ in range(6))
            matriz_aleatoria.append(fila)
        return matriz_aleatoria

    def sanar_mutantes(self, matriz):
        """
        Sanar cualquier mutante en la matriz de ADN.
        
        Si se detectan mutantes, genera un ADN completamente nuevo sin mutantes.
        
        :param matriz: La matriz de ADN a sanar.
        :return: Una nueva matriz de ADN sin mutantes.
        """
        detector = Detector('T')  # Aquí suponemos que estamos buscando mutantes de 'T'
        
        # Verificar si hay mutantes
        if detector.detectar_mutantes(matriz):
            print("Mutante detectado. Generando nuevo ADN...")
            # Generar un nuevo ADN aleatorio
            nuevo_adn = self.generar_adn_aleatorio()
            print("Nuevo ADN generado:")
            for fila in nuevo_adn:
                print(fila)
            return nuevo_adn
        else:
            print("No se detectaron mutantes.")
            return matriz  # Si no hay mutantes, devolver la matriz original
