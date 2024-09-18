#ESTA FUNCION DETERMINA LA CALIFICACION
def obtener_calificacion(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota < 90:
        return 'B'
    elif 70 <= nota < 80:
        return 'C'
    elif 60 <= nota < 70:
        return 'D'
    elif 0 <= nota < 60:
        return 'F'
    else:
        return None
#ESTA FUNCION SOLICITA AL USUARIO QUE INGRESE UNA CALIFICACION
def main():
    try:
        nota = float(input("Ingrese la calificación (0-100): "))
        
        calificacion = obtener_calificacion(nota)

        if calificacion is not None:
            print(f"La calificación correspondiente es: {calificacion}")
        else:
            print("La calificación ingresada no es válida. Debe estar entre 0 y 100.")

    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
