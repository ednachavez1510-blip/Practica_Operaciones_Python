# Nombre: Edna Lucia Chavez Vilchis
# Fecha: 14 Noviembre 2025
# Descripción: Práctica - Captura de datos y operaciones aritméticas básicas

# 1. Captura de datos del usuario
nombre = input("Ingresa tu nombre completo: ")
edad = input("Ingresa tu edad: ")
estatura = input("Ingresa tu estatura en metros (por ejemplo 1.70): ")
gusta_programar = input("¿Te gusta programar? Escribe True o False: ")

# 2. Conversión de tipos
edad = int(edad)
estatura = float(estatura)
gusta_programar = gusta_programar == "True"   # Convierte a booleano

# 3. Mostrar datos capturados
print("\n--- DATOS CAPTURADOS ---")
print("Nombre completo:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Le gusta programar?:", gusta_programar)

# 4. Mostrar tipo de cada dato
print("\n--- TIPOS DE DATOS ---")
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'estatura':", type(estatura))
print("Tipo de 'gusta_programar':", type(gusta_programar))