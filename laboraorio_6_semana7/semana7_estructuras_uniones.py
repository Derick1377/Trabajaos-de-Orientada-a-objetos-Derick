equipo = {
    "nombre": input("Nombre de la computadora: "),
    "ram": int(input("Cuanta RAM tiene (GB): ")),
    "estado": input("Estado de la computadora: ")
}

dato_alternativo = {
    "tipo": input("Tipo de identificador (serie/activo): "),
    "valor": input("Numero del identificador: ")
}

print("\nREGISTRO DE COMPUTADORA")
print("Nombre:", equipo["nombre"])
print("Memoria RAM:", equipo["ram"], "GB")
print("Estado:", equipo["estado"])
print("Identificador:", dato_alternativo["tipo"], "=", dato_alternativo["valor"])
