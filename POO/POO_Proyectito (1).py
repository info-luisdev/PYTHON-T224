import os

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
    FacturaID=1
    def __init__(self, monto_impuestos, total, productos):
        self.id=Factura.FacturaID
        self.monto_impuestos=monto_impuestos
        self.total=total
        self.productos=productos
        
    def imprimirProductos():
        for producto in productos:
            producto.mostrarProducto()

    def mostrarFactura(self):
        print("ID: ", self.id, " - Impuestos: ", self.monto_impuestos, " - Total: ", self.total)
        Factura.imprimirProductos()
        print("\n")

productos = []
productos.append(Producto("Arroz", 50, 100, "01"))
productos.append(Producto("Habichuelas", 60, 50, "01"))
productos.append(Producto("Aceite", 300, 30, "02"))
productos.append(Producto("Lechuga", 80, 75, "00"))
productos.append(Producto("Pollo", 90, 40, "01"))
productos.append(Producto("Agua", 20, 200, "00"))
productos.append(Producto("Coca-Cola", 30, 150, "01"))

facturas=[]

def imprimirMenu():
    print("Menú")
    for producto in productos:
        producto.mostrarProducto()

def buscar_producto(id):
    for producto in productos:
        if(producto.id==id):
            return producto
    return None

def calcular_factura(carrito):
    total=0
    for producto in carrito:
        total+=producto.getPrecio()
    impuestos=total*0.18
    return impuestos, total

def facturar():
    seguir_facturando=1
    while seguir_facturando==1:
        carrito=[]
        salir_o_no=1
        while salir_o_no==1:
            os.system("cls")
            imprimirMenu()
            opc=int(input("Ingresa el índice del producto que deseas: "))
            productoTemp=buscar_producto(opc)
            if (productoTemp):
                carrito.append(productoTemp)
            else:
                print("El producto no existe")
            salir_o_no=int(input("Deseas agregar más productos? 1. Sí 2. No: "))
        impuestos, total = calcular_factura(carrito)
        facturas.append(Factura(impuestos, total, carrito))
        seguir_facturando=int(input("Deseas seguir facturando? 1. Sí 2. No: "))

facturar()

for factura in facturas:
    factura.mostrarFactura()
