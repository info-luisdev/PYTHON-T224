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



