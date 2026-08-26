print("DROP KICKS PR")

print("-------------------------")

print("1. Nike Air Force 1 - $120")
print("2. Jordan 1 - $150")
print("3. New Balance 550 - $110")
print("4. Adidas Campus - $100")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    tenis = "Nike Air Force 1"
    precio = 120

elif opcion == 2:
    tenis = "Jordan 1"
    precio = 150

elif opcion == 3:
    tenis = "New Balance 550"
    precio = 110

elif opcion == 4:
    tenis = "Adidas Campus"
    precio = 100

else:
    print("Opción no válida.")
    exit()

print("\nTamaños disponibles:")

print("6")
print("7")
print("8")
print("9")
print("10")

size = input("Seleccione el tamaño: ")

print("Ingrese la cantidad:")
cantidad = int(input())

total = precio * cantidad

print("\n----- RESUMEN DE COMPRA -----")

print("Tenis:", tenis)
print("Size:", size)
print("Cantidad:", cantidad)
print("Precio: $", precio)
print("Total: $", total)
print("-----------------------------")
print("Gracias por su compra en DROP KICKS PR")