from clases import Detector, Radiacion, Virus, Sanador

def main():
    
    adn = []
    print("Ingresa la matriz de ADN (6 filas de 6 caracteres). Cada fila debe ser una cadena de 6 caracteres.")
    for i in range(6):
        while True:
            fila = input(f"Ingresar fila {i+1} de ADN (A, T, C, G): ").upper()
            if len(fila) == 6 and all(c in 'ATCG' for c in fila):
                adn.append(list(fila))
                break
            else:
                print("Entrada no válida. Asegúrate de ingresar una fila de 6 caracteres (A, T, C, G).")

    
    while True:
        print("\nElige una opción")
        print("1: Detectar mutaciones")
        print("2: Mutar ADN")
        print("3: Sanar ADN")
        print("4: Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            detector = Detector(adn)
            if detector.detectar_mutantes():
                print("Se detectaron mutaciones en el ADN.")
            else:
                print("No se detectaron mutaciones en el ADN.")

        elif opcion == "2":
            tipo_mutacion = input("¿Qué tipo de mutación deseas crear? (1: Radiación, 2: Virus): ")
            base_nitrogenada = input("Ingresa la base para la mutación (A, T, C, G): ").upper()
            while base_nitrogenada not in 'ATCG' or len(base_nitrogenada) != 1:
                print("Base no válida. Debe ser una sola letra de A, T, C o G.")
                base_nitrogenada = input("Ingresa la base para la mutación (A, T, C, G): ").upper()

            posicion = input("Ingresa la posición inicial (fila, columna): ").split(',')
            x, y = int(posicion[0]), int(posicion[1])

            orientacion = input("Ingresa la orientación de la mutación (H para horizontal, V para vertical): ").upper()
            while orientacion not in ['H', 'V']:
                print("Orientación no válida. Usa 'H' para horizontal o 'V' para vertical.")
                orientacion = input("Ingresa la orientación de la mutación (H para horizontal, V para vertical): ").upper()

            if tipo_mutacion == "1":
                mutador = Radiacion(base_nitrogenada, (x, y), orientacion)
            elif tipo_mutacion == "2":
                mutador = Virus(base_nitrogenada, (x, y))
            else:
                print("Opción no válida.")
                continue

            adn_mutado = mutador.crear_mutante(adn)
            print("El ADN mutado es:")
            for fila in adn_mutado:
                print(''.join(fila))

        elif opcion == "3":
            sanador = Sanador(adn) 
            adn_sano = sanador.sanar_mutantes()
            print("El ADN sano es:")
            for fila in adn_sano:
                print(''.join(fila))

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")

if __name__ == "__main__":
    main()