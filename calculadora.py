#Suma Michael
print("calculadora")
def suma(num1, num2):
    return (num1 + num2)
# /////////////////


# Resta Juan Jose
def resta (num1, num2):
    return (num1-num2)
# /////////////////


# Multiplicación Julián
def multiplicacion(num1, num2):
    multi = (num1 * num2)
    return multi
# /////////////////

# División
def division(num1, num2):
    div = (num1 / num2)
    return div
# /////////////////

print("Ingrese los dos números para la operación")
num1 = int(input())
num2 = int(input())

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

print("Escoja que operacion desea realizar:")
opcionEscogida = int(input())



if opcionEscogida == 1:
    resultado = suma(num1, num2)
    print("El resultado es: " + str(resultado))
elif opcionEscogida == 2:
    resultado = resta(num1, num2)
    print("El resultado es: " + str(resultado))
elif opcionEscogida == 3:
    resultado = multiplicacion(num1, num2)
    print("El resultado es: " + str(resultado))
elif opcionEscogida == 4:
    resultado = division(num1, num2)
    print("El resultado es: " + str(resultado))
else:
    print("Opción inválida")