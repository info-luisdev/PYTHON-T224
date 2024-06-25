class Cine:
    def __init__(self, id, nombre, cantidad_salas, provincia):
        self.__id = id
        self.__nombre = nombre
        self.__cantidad_salas = cantidad_salas
        self.__provincia = provincia
        self.__boletas = []

    def agregar_boleta(self, boleta):
        self.__boletas.append(boleta)

    def obtener_id(self):
        return self.__id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_cantidad_salas(self):
        return self.__cantidad_salas

    def obtener_provincia(self):
        return self.__provincia

    def obtener_boletas(self):
        return self.__boletas

    def total_recaudacion(self):
        try:
            return sum(boleta.obtener_precio() for boleta in self.__boletas)
        except ValueError:
            return 0

    def genero_mas_gustado(self):
        conteo_generos = {}
        for boleta in self.__boletas:
            genero = boleta.obtener_pelicula().obtener_genero()
            if genero in conteo_generos:
                conteo_generos[genero] += 1
            else:
                conteo_generos[genero] = 1
        genero_mas_gustado = max(conteo_generos, key=conteo_generos.get)
        return genero_mas_gustado


class Pelicula:
    def __init__(self, id, nombre, genero, duracion):
        self.__id = id
        self.__nombre = nombre
        self.__genero = genero
        self.__duracion = duracion

    def obtener_id(self):
        return self.__id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_genero(self):
        return self.__genero

    def obtener_duracion(self):
        return self.__duracion


class Boleta:
    def __init__(self, id, precio, pelicula, sala, asiento, hora, cliente):
        self.__id = id
        self.__precio = precio
        self.__pelicula = pelicula
        self.__sala = sala
        self.__asiento = asiento
        self.__hora = hora
        self.__cliente = cliente

    def obtener_id(self):
        return self.__id

    def obtener_precio(self):
        return self.__precio

    def obtener_pelicula(self):
        return self.__pelicula

    def obtener_sala(self):
        return self.__sala

    def obtener_asiento(self):
        return self.__asiento

    def obtener_hora(self):
        return self.__hora

    def obtener_cliente(self):
        return self.__cliente
