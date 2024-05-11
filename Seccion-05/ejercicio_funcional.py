menu = [
    {"id": 1, "desc": "Arroz", "precio": 50},
    {"id": 2, "desc": "Habichuelas", "precio": 60},
    {"id": 3, "desc": "Aceite", "precio": 300},
    {"id": 4, "desc": "Lechuga", "precio": 80},
    {"id": 5, "desc": "Pollo", "precio": 90},
    {"id": 6, "desc": "Agua", "precio": 20},
    {"id": 7, "desc": "Coca-Cola", "precio": 30}
]

def imprimir_menu(menu):
    for producto in menu:
        print(str(producto["id"]) + ".", producto["desc"], "->", producto["precio"])

def comprar(menu):
    carrito = []
    salir_o_no = 1
    while salir_o_no == 1:
        imprimir_menu(menu)
        opc = int(input("Ingresa el índice del producto que deseas: "))
        if buscar_producto(opc, menu) == -1:
            print("Opción inválida")
        else:
            cantidad = int(input("Ingresa la cantidad que deseas: "))
            if cantidad <= 0:
                print("Cantidad inválida")
            else:
                producto = buscar_producto(opc, menu)
                producto_en_carrito = buscar_producto_en_carrito(producto, carrito)
                if producto_en_carrito:
                    producto_en_carrito["cantidad"] += cantidad  
                else:
                    producto["cantidad"] = cantidad  
                    carrito.append(producto)
        salir_o_no = int(input("Deseas agregar más productos? 1. Sí 2. No: "))
    return carrito

def imprimir_factura(carrito):
    print("Factura:")
    print("-" * 50)
    print("{:<5} {:<15} {:<10} {:<10} {:<10}".format("ID", "Descripción", "Precio", "Cantidad", "Total"))
    subtotal = 0
    for producto in carrito:
        total_producto = producto["precio"] * producto["cantidad"]
        subtotal += total_producto
        print("{:<5} {:<15} {:<10} {:<10} {:<10}".format(producto["id"], producto["desc"], producto["precio"], producto["cantidad"], total_producto))
    print("-" * 50)
    impuestos = subtotal * 0.18
    total = subtotal + impuestos
    print("{:<30} {:<20}".format("Subtotal:", subtotal))
    print("{:<30} {:<20}".format("Impuestos (18%):", impuestos))
    print("{:<30} {:<20}".format("Total:", total))
    print("-" * 50)

def buscar_producto(id, menu):
    for producto in menu:
        if producto["id"] == id:
            return producto
    return -1

def buscar_producto_en_carrito(producto, carrito):
    for item in carrito:
        if item["id"] == producto["id"]:
            return item
    return None

productos = comprar(menu)
imprimir_factura(productos)
