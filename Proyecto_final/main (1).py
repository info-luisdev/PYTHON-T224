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

    def listar_reserva(self):
        return {
            "id": self.id,
            "nombre_cliente": self.cliente.nombre,
            "numero_personas": self.numero_personas,
            "fecha": self.fecha,
            "mesa": self.mesa
        }
