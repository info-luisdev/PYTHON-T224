import json

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Reserva:
    def __init__(self, id, cliente, numero_personas, fecha, mesa):
        self.id = id
        self.cliente = cliente
        self.numero_personas = numero_personas
        self.fecha = fecha
        self.mesa = mesa

    def reserva_json(self):
        return {
            "id": self.id,
            "nombre_cliente": self.cliente.nombre,
            "numero_personas": self.numero_personas,
            "fecha": self.fecha,
            "mesa": self.mesa
        }

class Reservaciones:
    def __init__(self):
        self.reservas = []
        self.mesas_disponibles = list(range(1, 41))
        self.id_reserva = 1
        self.load_reservas()

    def load_reservas(self):
        try:
            with open("reservas.json", "r") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    cliente = Cliente(item['nombre_cliente'])
                    reserva = Reserva(item['id'], cliente, item['numero_personas'], item['fecha'], item['mesa'])
                    self.reservas.append(reserva)
                    self.mesas_disponibles.remove(reserva.mesa)
                if self.reservas:
                    self.id_reserva = max(reserva.id for reserva in self.reservas) + 1
        except FileNotFoundError:
            self.reservas = []

    def guardar_reservas(self):
        datos = [reserva.reserva_json() for reserva in self.reservas]
        with open("reservas.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def mostrar_menu(self):
        print("\nMenú de Reservaciones Restaurante el Coco:")
        print("1. Añadir Reserva")
        print("2. Visualizar Reservas Activas")
        print("3. Anular Reserva ")
        print("4. Salir del Programa")

    def añadir_reserva(self):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        numero_personas = int(input("Ingrese el número de personas: "))
        fecha = input("Ingrese la fecha de la reserva (DD/MM/YYYY): ")

        if numero_personas <= 0:
            print("El número de personas debe ser mayor que cero.")
            return
        
        if not self.mesas_disponibles:
            print("No hay mesas disponibles.")
            return

        print(f"Mesas disponibles: {self.mesas_disponibles}")
        mesa = int(input("Seleccione una mesa de las disponibles: "))

        if mesa not in self.mesas_disponibles:
            print("Mesa no disponible.")
            return

        cliente = Cliente(nombre_cliente)
        nueva_reserva = Reserva(self.id_reserva, cliente, numero_personas, fecha, mesa)
        self.reservas.append(nueva_reserva)
        self.mesas_disponibles.remove(mesa)
        self.id_reserva += 1
        print(f"Reserva creada exitosamente para {nombre_cliente} en la mesa {mesa} el {fecha}.")
        self.guardar_reservas()

    def presentar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
        else:
            print("\nListado de reservas:")
            for reserva in self.reservas:
                print(f"ID: {reserva.id}, Cliente: {reserva.cliente.nombre}, Personas: {reserva.numero_personas}, Fecha: {reserva.fecha}, Mesa: {reserva.mesa}")

    def anular_reserva(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return

        id_reserva = int(input("Ingrese el ID de la reserva a cancelar: "))
        reserva_encontrada = None
        for reserva in self.reservas:
            if reserva.id == id_reserva:
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            self.reservas.remove(reserva_encontrada)
            self.mesas_disponibles.append(reserva_encontrada.mesa)
            print(f"Reserva con ID {id_reserva} cancelada.")
            self.añadir_reserva()
        else:
            print(f"Reserva con ID {id_reserva} no encontrada.")

    def main(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                self.añadir_reserva()
            elif opcion == "2":
                self.presentar_reservas()
            elif opcion == "3":
                self.anular_reserva()
            elif opcion == "4":
                print("Sistema Cerrado")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    agendar_reserva = Reservaciones()
    agendar_reserva.main()
