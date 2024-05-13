import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    opcion = ""
    while opcion != 'e':
        print("Selecciona una opción:")
        print("a) Calcular área de un rectángulo")
        print("b) Calcular el área de un círculo")
        print("c) Calcular el área de un triángulo")
        print("e) Salir del programa")
        opcion = input("\nOpción seleccionada: ")

        if opcion == 'a':
            base = float(input("Ingresa la base del rectángulo: "))
            altura = float(input("Ingresa la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es :" , area)
        elif opcion == 'b':
            radio = float(input("Ingresa el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es: " , area)
        elif opcion == 'c':
            base = float(input("Ingresa la base del triángulo: "))
            altura = float(input("Ingresa la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es: " , area)
        elif opcion == 'e':
            print("SALIENDO")
        else:
            print("Ingrese otra opción válida por favor (otro número)")

if __name__ == "__main__":
    main()
