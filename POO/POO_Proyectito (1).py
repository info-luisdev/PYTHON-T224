import os
from datetime import datetime

class Producto:
    ProductID = 1

    def __init__(self, desc, precio, existencia, impuesto):
        self.id = Producto.ProductID
        self.desc = desc
        self.precio = precio
        self.existencia = existencia
        self.impuesto = impuesto
        Producto.ProductID += 1

    def mostrar_producto(self):
        print(f"ID: {self.id} - Nombre: {self.desc} - Precio: {self.precio} - existencia: {self.existencia} - Impuesto: {self.impuesto}")

    def get_precio(self):
        return self.precio

    def get_id(self):
        return self.id

    def get_desc(self):
        return self.desc

    def get_impuesto(self):
        return self.impuesto

    def get_existencia(self):
        return self.existencia

    def reducir_existencia(self, cantidad):
        self.existencia -= cantidad

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        encontrado = False
        for item in self.productos:
            if item['producto'].get_id() == producto.get_id():
                item['cantidad'] += cantidad
                encontrado = True
                break
        if not encontrado:
            self.productos.append({'producto': producto, 'cantidad': cantidad})

    def mostrar_carrito(self):
        for item in self.productos:
            producto = item['producto']
            cantidad = item['cantidad']
            total_producto = producto.get_precio() * cantidad
            print(f"ID: {producto.get_id()} - Nombre: {producto.get_desc()} - Precio: {producto.get_precio()} - Cantidad: {cantidad} - Total: {total_producto}")

    def calcular_total(self):
        subtotal = 0
        impuestos = 0
        for item in self.productos:
            precio_total = item['producto'].get_precio() * item['cantidad']
            subtotal += precio_total
            if item['producto'].get_impuesto() == "01":
                impuestos += precio_total * 0.18
            elif item['producto'].get_impuesto() == "02":
                impuestos += precio_total * 0.16
        total = subtotal + impuestos
        return subtotal, impuestos, total

    def vaciar_carrito(self):
        self.productos = []

class Factura:
    FacturaID = 1

    def __init__(self, cliente, carrito):
        self.id = Factura.FacturaID
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cliente = cliente
        self.carrito = carrito
        self.subtotal, self.monto_impuestos, self.total = carrito.calcular_total()
        Factura.FacturaID += 1

    def mostrar_factura(self):
        print(f"Factura ID: {self.id}")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print("-" * 50)
        print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("ID", "Descripción", "Precio", "Cantidad", "Total"))
        for item in self.carrito.productos:
            producto = item['producto']
            cantidad = item['cantidad']
            total_producto = producto.get_precio() * cantidad
            print("{:<5} {:<15} {:<10} {:<10} {:<10}".format(producto.get_id(), producto.get_desc(), producto.get_precio(), cantidad, total_producto))
        print("-" * 50)
        print("{:<30} {:<20}".format("Subtotal:", self.subtotal))
        print("{:<30} {:<20}".format("Impuestos:", self.monto_impuestos))
        print("{:<30} {:<20}".format("Total:", self.total))
        print("-" * 50)


productos = []
productos.append(Producto("Arroz", 50, 100, "01"))
productos.append(Producto("Habichuelas", 60, 50, "01"))
productos.append(Producto("Aceite", 300, 30, "02"))
productos.append(Producto("Lechuga", 80, 75, "00"))
productos.append(Producto("Pollo", 90, 40, "01"))
productos.append(Producto("Agua", 20, 200, "00"))
productos.append(Producto("Coca-Cola", 30, 150, "01"))

facturas = []

def imprimir_menu():
    print("Menú Surtidora ITLA Santiago SRL")
    for producto in productos:
        producto.mostrar_producto()

def buscar_producto(id):
    for producto in productos:
        if producto.get_id() == id:
            return producto
    return None

def facturar():
    cliente = input("Ingrese el nombre del cliente: ")
    carrito = Carrito()
    seguir_facturando = True

    while seguir_facturando:
        os.system("cls")
        imprimir_menu()
        opc = int(input("Ingresa el índice del producto que deseas: "))
        producto = buscar_producto(opc)
        if producto:
            cantidad = int(input(f"Ingrese la cantidad de {producto.get_desc()} que desea (existencia disponible: {producto.get_existencia()}): "))
            if cantidad > 0 and cantidad <= producto.get_existencia():
                carrito.agregar_producto(producto, cantidad)
                producto.reducir_existencia(cantidad)
            else:
                print("Cantidad inválida o insuficiente existencia.")
        else:
            print("Producto no encontrado.")
        
        seguir = input("¿Deseas agregar más productos? (S/N): ").lower()
        if seguir != 's':
            seguir_facturando = False

    factura = Factura(cliente, carrito)
    facturas.append(factura)
    factura.mostrar_factura()
    carrito.vaciar_carrito()
    
os.system('cls')

salir_del_sistema = int(input('Necesita imprimir Una factura: 1. Si / 2. No: '))

while salir_del_sistema == 1:
    facturar()
    salir_del_sistema = int(input('Necesita imprimir Otra factura: 1. Si / 2. No: '))
    os.system('cls')

