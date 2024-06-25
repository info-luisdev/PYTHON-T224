import json
from clases import Cine, Pelicula, Boleta

class Main:
    def __init__(self):
        self.__cines = []
        self.__peliculas = []
        self.__exportar_datos()

    def __exportar_datos(self):
        try:
            with open('datos.json', 'r') as file:
                datos = json.load(file)
            
            for pelicula_data in datos['peliculas']:
                pelicula = Pelicula(
                    pelicula_data['id'],
                    pelicula_data['nombre'],
                    pelicula_data['genero'],
                    pelicula_data['duracion']
                )
                self.__peliculas.append(pelicula)

            for cine_data in datos['cines']:
                cine = Cine(
                    cine_data['id'],
                    cine_data['nombre'],
                    cine_data['cantidad_salas'],
                    cine_data['provincia']
                )
                boletas_vendidas = cine_data.get('boletas_vendidas', 0)
                for i in range(boletas_vendidas):
                    boleta = Boleta(
                        id=str(i + 1),
                        precio=300,
                        pelicula=self.__peliculas[i % len(self.__peliculas)],
                        sala=i % cine_data['cantidad_salas'] + 1,
                        asiento=f"A{i + 1}",
                        hora=f"{i % 12 + 8}:00",
                        cliente="Cliente"
                    )
                    cine.agregar_boleta(boleta)

                self.__cines.append(cine)
        
        except FileNotFoundError:
            print("Error: No se encontró el archivo 'datos.json'.")
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error al cargar los datos: {str(e)}")

    def __obtener_cine_por_id(self, codigo_cine):
        for cine in self.__cines:
            if cine.obtener_id() == codigo_cine:
                return cine
        return None

    def max_proyecciones(self, nombre_pelicula):
        nombre_pelicula = nombre_pelicula.lower()
        conteo_proyecciones = {}
        for cine in self.__cines:
            for boleta in cine.obtener_boletas():
                if boleta.obtener_pelicula().obtener_nombre().lower() == nombre_pelicula:
                    if cine.obtener_nombre() in conteo_proyecciones:
                        conteo_proyecciones[cine.obtener_nombre()] += 1
                    else:
                        conteo_proyecciones[cine.obtener_nombre()] = 1
        if conteo_proyecciones:
            cine_mas_proyecciones = max(
                conteo_proyecciones, key=conteo_proyecciones.get
            )
            return cine_mas_proyecciones
        return None

    def menu(self):
        print("\nMenú:")
        print("1. Cine con mayor recaudación")
        print("2. Total Vendido")
        print("3. Género más vistos")
        print("4. Cine con pelicula mas proyectada")
        print("5. Salir del sistema")

    def correr(self):
        while True:
            self.menu()
            opcion = input("Seleccione una opción válida: ")

            if opcion == "1":
                cine = self.max_vendido_cine()
                if cine:
                    print(f"Cine con mayor recaudación: {cine.obtener_nombre()}, Provincia: {cine.obtener_provincia()} con RD${cine.total_recaudacion()}")
                else:
                    print("No hay datos disponibles.")
            
            elif opcion == "2":
                total_ventas = self.total_vendido()
                print(f"Total vendido: Pesos${total_ventas}")
            
            elif opcion == "3":
                codigo_cine = input("Ingrese el id del cine: ")
                genero = self.genero_mejor_valorado(codigo_cine)
                if genero:
                    print(f"Género mejor valorado {codigo_cine}: {genero}")
                else:
                    print("No hay datos coincidentes con su petición.")
            
            elif opcion == "4":
                nombre_pelicula = input("Ingrese el nombre de la película: ")
                cine = self.max_proyecciones(nombre_pelicula)
                if cine:
                    print(f"Cine con más proyecciones de {nombre_pelicula}: {cine}")
                else:
                    print("Error, Dato no encontrado")
            
            elif opcion == "5":
                print("Sistema Cerrado")
                break
            
            else:
                print("Opción inválida.")

    def max_vendido_cine(self):
        if not self.__cines:
            return None
        
        cine_max_recaudacion = max(self.__cines, key=lambda cine: cine.total_recaudacion(), default=None)
        return cine_max_recaudacion

    def total_vendido(self):
        return sum(map(lambda cine: cine.total_recaudacion(), self.__cines))

    def genero_mejor_valorado(self, codigo_cine):
        cine = next(filter(lambda x: x.obtener_id() == codigo_cine, self.__cines), None)
        if cine:
            return cine.genero_mas_gustado()
        return None


if __name__ == "__main__":
    main = Main()
    main.correr()
