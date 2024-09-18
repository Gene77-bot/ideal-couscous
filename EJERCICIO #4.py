def calcular_salario(semanal, horas_trabajadas, salario_por_hora):
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario_semanal = (40 * salario_por_hora) + (horas_extras * salario_por_hora * 1.5)
    else:
#ESTA FUNCION CALCULA EL SALARIO SEMANAL BASADAS EN LAS HORAS TRABAJADAS

        salario_semanal = horas_trabajadas * salario_por_hora

    # Añadir bono especial si aplica
    if salario_por_hora in [60, 70] and horas_trabajadas > 50:
        salario_semanal += 200

    return salario_semanal

#PRESENTA AL USUARIO EL TIPO DE SALARIO DISPONIBLE 
def main():
    # Definición de salarios
    salarios = {
        'A': 60,
        'B': 70,
        'C': 120
    }
    
    print("Tipos de salarios disponibles:")
    for tipo, salario in salarios.items():
        print(f"Salario {tipo}: {salario} por hora")

    tipo_salario = input("Ingrese el tipo de salario (A, B o C): ").upper()
    
    if tipo_salario in salarios:
        salario_por_hora = salarios[tipo_salario]
        try:
            horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))
            if horas_trabajadas < 0:
                print("Las horas trabajadas no pueden ser negativas.")
                return
            
            salario_semanal = calcular_salario(salario_por_hora, horas_trabajadas, salario_por_hora)
            print(f"El salario semanal es: ${salario_semanal:.2f}")

        #ESTA FUNCION VALIDA LOS SALARIOS CORRECTOS O DISPONIBLES
        except ValueError:
            print("Por favor, ingrese un número válido para las horas trabajadas.")
    else:
        print("Tipo de salario no válido. Debe ser A, B o C.")

if __name__ == "__main__":
    main()
