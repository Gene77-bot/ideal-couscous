#Calcula la diferencia absoluta entre el presupuesto y el precio del proyecto
def calcular_factibilidad(presupuesto, precio_proyecto):
    # Calcular la diferencia porcentual
    diferencia = abs(presupuesto - precio_proyecto)
    porcentaje_diferencia = (diferencia / presupuesto) * 100
    
    # Determinar si es factible
    if porcentaje_diferencia < 75:
        return True, porcentaje_diferencia
    else:
        return False, porcentaje_diferencia
    
#Solicita al usuario que ingrese el presupuesto y el precio del proyecto
def main():
    try:
        presupuesto = float(input("Ingrese el presupuesto del proyecto: "))
        precio_proyecto = float(input("Ingrese el precio del proyecto: "))
        
        if presupuesto <= 0 or precio_proyecto < 0:
            print("El presupuesto debe ser mayor que cero y el precio del proyecto no puede ser negativo.")
            return
        
        factible, porcentaje = calcular_factibilidad(presupuesto, precio_proyecto)
        
        if factible:
            print(f"El proyecto es factible. La diferencia porcentual es del {porcentaje:.2f}%.")
        else:
            print(f"El proyecto no es factible. La diferencia porcentual es del {porcentaje:.2f}%.")

 #Se incluye un bloque try-except para manejar entradas no válidas y asegurar que el programa no falle
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
