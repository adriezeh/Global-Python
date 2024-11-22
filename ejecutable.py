from clases import Detector, Radiacion, Virus, Sanador

def mostrar_adn(matriz):
    """Muestra la matriz de ADN de forma legible."""
    for fila in matriz:
        print(' '.join(fila))

def main():
 
    adn_usuario = []
    print("Por favor ingresa el ADN (una matriz de 5x5), fila por fila:")
    for i in range(5):
        fila = input(f"Ingrese la fila {i+1} del ADN (separada por espacios): ").split()
        adn_usuario.append(fila)

    while True:
        print("\n¿Que deseas hacer?")
        print("1. Detectar mutaciones")
        print("2. Mutar el ADN")
        print("3. Sanar el ADN")
        print("4. Salir")
        opcion = input("Ingresa el numero de la opcion: ")

        if opcion == "1":
            detector = Detector()
            if detector.detectar_mutantes(adn_usuario):
                print("Se han detectado mutaciones!!")
            else:
                print("No se detectaron mutaciones.")
        
        elif opcion == "2":
            tipo_mutacion = input("¿Que tipo de mutacion deseas crear? (Radiacion / Virus): ").strip().capitalize()
            base_nitrogenada = input("Ingresa la base nitrogenada para la mutación (A, T, C, G): ").upper()
            posicion_inicial = tuple(map(int, input("Ingresa la posición inicial (fila, columna) separada por coma: ").split(',')))
            if tipo_mutacion == "Radiacion":
                orientacion = input("Ingresa la orientacion de la mutacion (H para horizontal, V para vertical): ").upper()
                radiacion = Radiacion(base_nitrogenada, 10)
                adn_usuario = radiacion.crear_mutante(base_nitrogenada, posicion_inicial, orientacion)
            elif tipo_mutacion == "Virus":
                virus = Virus(base_nitrogenada, 5)
                adn_usuario = virus.crear_mutante(base_nitrogenada, posicion_inicial)
            mostrar_adn(adn_usuario)
        
        elif opcion == "3":
            sanador = Sanador()
            adn_usuario = sanador.sanar_mutantes(adn_usuario)
            print("ADN sanado:")
            mostrar_adn(adn_usuario)
        
        elif opcion == "4":
            print("Hasta luego")
            break
        else:
            print("Opcion no valida. Intenta nuevamente.")

if __name__ == "__main__":
    main()