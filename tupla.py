# Tupla de colores (una colección ordenada )
colores = ("amarillo", "azul", "morado", "blanco", "rojo")

# Mostrar la tupla completa
print("Tupla completa de colores:")
print(colores)

# Acceder a elementos individuales por índice
print("\nAcceso individual:")
print("Primer color:", colores[0])      # amarillo
print("Segundo color:", colores[1])     # azul
print("Tercer color:", colores[2])      # morado
print("Último color:", colores[-1])     # rojo (índice negativo)

# Recorrer la tupla con un bucle
print("\nColores uno por uno:")
for color in colores:
    print(f"- {color}")
