class Computadora:
    def __init__(self, marca, modelo, ram, estado):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.estado = estado

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("RAM:", self.ram, "GB")
        print("Estado:", self.estado)
        print()

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ("Disponible", "En reparacion"):
            self.estado = nuevo_estado
            print("Estado cambiado a:", self.estado)
        else:
            print("Ese estado no esta permitido")


computadora1 = Computadora("Acer", "Predator", 16, "Disponible")
computadora2 = Computadora("Dell", "Inspiron", 8, "En reparacion")
computadora3 = Computadora("HP", "Pavilion", 32, "Disponible")

print("--- DATOS DE LAS TRES COMPUTADORAS ---")
computadora1.mostrar_datos()
computadora2.mostrar_datos()
computadora3.mostrar_datos()

print("--- CAMBIAR EL ESTADO DE LA PRIMERA ---")
computadora1.cambiar_estado("En reparacion")

print("\n--- COMPROBAR QUE LAS OTRAS NO CAMBIARON ---")
computadora1.mostrar_datos()
computadora2.mostrar_datos()
computadora3.mostrar_datos()

print("--- PROBAR UN ESTADO NO PERMITIDO ---")
computadora1.cambiar_estado("Dañada")
computadora1.mostrar_datos()
