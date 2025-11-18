"""
Demostración de variables simples en Python.

Este script imprime información básica sobre varias variables:
un número entero, un número flotante, una cadena de texto y
un valor booleano. Se utilizan f-strings y especificadores de
formato para mostrar los valores de manera clara y con el
número de decimales deseado en el caso del flotante.
"""

# Mostrar saludos iniciales
print("Hola")
print("Miguel")

# Inicializar variables
numero: int = 100
decimal: float = 78.2
cadena: str = "Hola"
estado: bool = True

# Mostrar información sobre los tipos de variables
print("Tipos de Variables\n")
# Imprimir el valor entero directamente
print(f"Variable de tipo entera: {numero}")
# Formatear el flotante con dos decimales
print(f"Variable de tipo flotante: {decimal:.2f}")
# Cadena de texto tal cual
print(f"Variable de tipo cadena: {cadena}")
# Mostrar el booleano como True/False en lugar de 1/0
print(f"Variable de tipo booleana: {estado}")



