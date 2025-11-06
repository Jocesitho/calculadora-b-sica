# calculadora.py
# Calculadora básica mejorada con manejo de errores y funciones

def solicitar_numero(mensaje):
    """Solicita un número al usuario y valida que sea un valor numérico."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Ingresa un número válido.")

def realizar_operacion(a, b, operacion):
    """Ejecuta la operación matemática seleccionada."""
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b == 0:
            return "Error: no se puede dividir por cero."
        return a / b
    else:
        return "Operación no válida."

def main():
    print("=== CALCULADORA BÁSICA ===")
    numero_1 = solicitar_numero("Primer número: ")
    numero_2 = solicitar_numero("Segundo número: ")
    operacion = input("Operación (+, -, *, /): ").strip()

    resultado = realizar_operacion(numero_1, numero_2, operacion)
    print("Resultado:", resultado)

if __name__ == "__main__":
    main()
