print("DROP KICKS PR")
print("LABORATORIO 5 - SEMANA 6")

# Parte 2 - Arreglo unidimensional
# Guardo cinco precios de tenis en una lista.

precios = [120, 150, 110, 100, 95]

print("\nPrecios de tenis:", precios)
print("Primer precio:", precios[0])
print("Tercer precio:", precios[2])

precios[4] = 90
print("Precios despues del cambio:", precios)

print("Todos los precios:")
for precio in precios:
    print(precio)


# Parte 3 - Arreglo multidimensional
# Cada fila es un dia y cada posicion es un modelo de tenis.

ventas = [
    [3, 5, 2],
    [4, 6, 3]
]

print("\nVentas de tenis")
print("Venta del dia 1 del modelo 2:", ventas[0][1])

for dia in range(2):
    print("Dia", dia + 1)
    for modelo in range(3):
        print("Modelo", modelo + 1, ":", ventas[dia][modelo])


# Parte 4 - Cadenas de caracteres

nombre = input("\nEscribe el nombre de unos tenis: ")

print("Cantidad de caracteres:", len(nombre))

if len(nombre) > 0:
    print("Primera letra:", nombre[0])
else:
    print("No escribiste un nombre.")

print("Letras del nombre:")
for letra in nombre:
    print(letra)

if "nike" in nombre.lower():
    print("El nombre tiene Nike")
else:
    print("El nombre no tiene Nike")

print("Nombre en mayusculas:", nombre.upper())
