#ESTA FUNCION TOMA LA PUNTUACION DEL EMPELADO Y DETERMINA SU NUVEL DE RENDIMIENTO
def evaluar_rendimiento(puntuacion):
    if puntuacion < 0.0 or puntuacion > 1.0:
        return "Puntuación no válida", 0.0

    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
    else:
        nivel = "Inaceptable"  # En caso de que se use un valor entre 0.0 y 0.4

    cantidad_dinero = 2400 * puntuacion
    return nivel, cantidad_dinero
# ESTA FUNCION SOLICITA QUE INGRESE LA PUNTUACION DEL USUARIO 
def main():
    try:
        puntuacion = float(input("Ingrese la puntuación del empleado (0.0, 0.4, 0.6 o más): "))
        
        nivel, cantidad_dinero = evaluar_rendimiento(puntuacion)

        if cantidad_dinero > 0:
            print(f"\nNivel de rendimiento: {nivel}")
            print(f"Cantidad de dinero a recibir: €{cantidad_dinero:.2f}")
        else:
            print("\n" + nivel)  # Mensaje de puntuación no válida

    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
