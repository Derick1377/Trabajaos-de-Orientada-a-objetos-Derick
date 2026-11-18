# TESI 2105 - Semana 11 - Laboratorio 9
# Guardar y recuperar notas usando archivos de texto.
import sys


class RegistroNotas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return None
        return sum(self.notas) / len(self.notas)


def mostrar_reporte(registro):
    promedio = registro.calcular_promedio()
    if promedio is None:
        print(f"{registro.nombre}: sin notas")
        print("Estado: sin notas")
    else:
        print(f"{registro.nombre}: {promedio:.1f}")
        if promedio >= 70:
            print("Estado: aprobado")
        else:
            print("Estado: en proceso")


def guardar_registros(registros, archivo):
    # Cada linea guarda: nombre|nota,nota (o solo nombre| si no tiene notas).
    with open(archivo, "w", encoding="utf-8") as salida:
        for registro in registros:
            notas = ",".join(str(nota) for nota in registro.notas)
            salida.write(f"{registro.nombre}|{notas}\n")
    print("Registros guardados en", archivo)


def cargar_registros(archivo):
    registros = []
    try:
        with open(archivo, "r", encoding="utf-8") as entrada:
            for numero_linea, linea in enumerate(entrada, 1):
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split("|")
                if len(partes) != 2 or not partes[0].strip():
                    raise ValueError(f"linea {numero_linea} con formato incorrecto")
                nombre, notas_texto = partes
                registro = RegistroNotas(nombre)
                if notas_texto:
                    for nota_texto in notas_texto.split(","):
                        nota = float(nota_texto)
                        if not 0 <= nota <= 100:
                            raise ValueError(f"nota fuera de rango en linea {numero_linea}")
                        registro.agregar(nota)
                registros.append(registro)
    except FileNotFoundError:
        print("Error: No se encontro el archivo", archivo)
        return None
    except ValueError as error:
        print("Error: El archivo tiene un dato incorrecto:", error)
        return None
    print("Registros recuperados de", archivo)
    return registros


def crear_ejemplos():
    ana = RegistroNotas("Ana")
    ana.agregar(90)
    ana.agregar(80)
    luis = RegistroNotas("Luis")
    luis.agregar(50)
    luis.agregar(60)
    eva = RegistroNotas("Eva")
    return [ana, luis, eva]


def main():
    archivo = "registro_notas_semana11.txt"
    accion = sys.argv[1] if len(sys.argv) > 1 else "guardar"

    if accion == "guardar":
        registros = crear_ejemplos()
        guardar_registros(registros, archivo)
        print("Datos guardados. Ejecuta de nuevo con 'cargar' para recuperarlos.")
    elif accion == "cargar":
        registros = cargar_registros(archivo)
        if registros is not None:
            for registro in registros:
                mostrar_reporte(registro)
    else:
        print("Usa: python TESI2105_S11_RegistroNotas_RamosDerick.py guardar")
        print("  o: python TESI2105_S11_RegistroNotas_RamosDerick.py cargar")


if __name__ == "__main__":
    main()