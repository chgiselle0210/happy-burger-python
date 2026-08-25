"""Interfaz de consola para administrar Happy Burger."""

import sqlite3

from database import crear_tablas
from modelos import Cliente, Menu, Pedido


def mostrar_encabezado(titulo):
    """Muestra un encabezado uniforme para cada sección."""
    print("\n" + "=" * 55)
    print(f"{titulo:^55}")
    print("=" * 55)


def pausar():
    """Detiene temporalmente el flujo para mostrar los resultados."""
    input("\nPresiona Enter para continuar...")


def mostrar_clientes():
    """Presenta los clientes registrados en la base de datos."""
    clientes = Cliente.listar_clientes()

    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\nClientes registrados:")
    print("-" * 55)

    for cliente in clientes:
        print(
            f"{cliente['clave']} | {cliente['nombre']} | "
            f"{cliente['correo_electronico']} | {cliente['telefono']}"
        )


def agregar_cliente():
    """Solicita y registra los datos de un cliente."""
    mostrar_encabezado("AGREGAR CLIENTE")

    cliente = Cliente(
        input("Clave: "),
        input("Nombre: "),
        input("Dirección: "),
        input("Correo electrónico: "),
        input("Teléfono: "),
    )

    cliente.agregar_cliente()
    print("\nCliente registrado correctamente.")


def actualizar_cliente():
    """Solicita los datos actualizados de un cliente."""
    mostrar_encabezado("ACTUALIZAR CLIENTE")
    mostrar_clientes()

    clave = input("\nClave del cliente que deseas actualizar: ").strip()

    if Cliente.buscar_cliente(clave) is None:
        print("\nNo existe un cliente con esa clave.")
        return

    cliente = Cliente(
        clave,
        input("Nuevo nombre: "),
        input("Nueva dirección: "),
        input("Nuevo correo electrónico: "),
        input("Nuevo teléfono: "),
    )

    cliente.actualizar_cliente()
    print("\nCliente actualizado correctamente.")


def eliminar_cliente():
    """Solicita la clave y elimina al cliente correspondiente."""
    mostrar_encabezado("ELIMINAR CLIENTE")
    mostrar_clientes()

    clave = input("\nClave del cliente que deseas eliminar: ").strip()

    if Cliente.eliminar_cliente(clave):
        print("\nCliente eliminado correctamente.")
    else:
        print("\nNo existe un cliente con esa clave.")


def menu_clientes():
    """Controla las operaciones disponibles para clientes."""
    while True:
        mostrar_encabezado("ADMINISTRACIÓN DE CLIENTES")
        print("1. Agregar cliente")
        print("2. Actualizar cliente")
        print("3. Eliminar cliente")
        print("4. Mostrar clientes")
        print("5. Regresar")

        opcion = input("\nSelecciona una opción: ").strip()

        try:
            if opcion == "1":
                agregar_cliente()
            elif opcion == "2":
                actualizar_cliente()
            elif opcion == "3":
                eliminar_cliente()
            elif opcion == "4":
                mostrar_encabezado("DIRECTORIO DE CLIENTES")
                mostrar_clientes()
            elif opcion == "5":
                return
            else:
                print("\nOpción no válida.")
        except (ValueError, sqlite3.Error) as error:
            print(f"\nNo fue posible realizar la operación: {error}")

        if opcion != "5":
            pausar()


def mostrar_productos():
    """Presenta los productos registrados en el menú."""
    productos = Menu.listar_productos()

    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\nProductos disponibles:")
    print("-" * 55)

    for producto in productos:
        print(
            f"{producto['clave']} | {producto['nombre']} | "
            f"${producto['precio']:.2f}"
        )


def agregar_producto():
    """Solicita y registra un producto en el menú."""
    mostrar_encabezado("AGREGAR PRODUCTO")

    producto = Menu(
        input("Clave: "),
        input("Nombre: "),
        input("Precio: $"),
    )

    producto.agregar_producto()
    print("\nProducto registrado correctamente.")


def actualizar_producto():
    """Solicita los datos actualizados de un producto."""
    mostrar_encabezado("ACTUALIZAR PRODUCTO")
    mostrar_productos()

    clave = input("\nClave del producto que deseas actualizar: ").strip()

    if Menu.buscar_producto(clave) is None:
        print("\nNo existe un producto con esa clave.")
        return

    producto = Menu(
        clave,
        input("Nuevo nombre: "),
        input("Nuevo precio: $"),
    )

    producto.actualizar_producto()
    print("\nProducto actualizado correctamente.")


def eliminar_producto():
    """Solicita la clave y elimina el producto correspondiente."""
    mostrar_encabezado("ELIMINAR PRODUCTO")
    mostrar_productos()

    clave = input("\nClave del producto que deseas eliminar: ").strip()

    if Menu.eliminar_producto(clave):
        print("\nProducto eliminado correctamente.")
    else:
        print("\nNo existe un producto con esa clave.")


def menu_productos():
    """Controla las operaciones disponibles para los productos."""
    while True:
        mostrar_encabezado("ADMINISTRACIÓN DEL MENÚ")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Regresar")

        opcion = input("\nSelecciona una opción: ").strip()

        try:
            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                actualizar_producto()
            elif opcion == "3":
                eliminar_producto()
            elif opcion == "4":
                mostrar_encabezado("MENÚ DE PRODUCTOS")
                mostrar_productos()
            elif opcion == "5":
                return
            else:
                print("\nOpción no válida.")
        except (ValueError, sqlite3.Error) as error:
            print(f"\nNo fue posible realizar la operación: {error}")

        if opcion != "5":
            pausar()


def imprimir_pedido(pedido):
    """Presenta los datos principales de un pedido."""
    if pedido is None:
        print("\nNo existe un pedido con ese número.")
        return

    print("-" * 55)
    print(f"Número: {pedido['pedido']}")
    print(f"Cliente: {pedido['cliente']}")
    print(f"Producto: {pedido['producto']}")
    print(f"Precio unitario: ${pedido['precio']:.2f}")
    print(f"Cantidad: {pedido['cantidad']}")
    print(f"Total: ${pedido['total']:.2f}")
    print(f"Estado: {pedido['estado']}")
    print(f"Fecha: {pedido['fecha_creacion']}")


def mostrar_pedidos():
    """Presenta todos los pedidos registrados."""
    pedidos = Pedido.listar_pedidos()

    if not pedidos:
        print("\nNo hay pedidos registrados.")
        return

    print()

    for pedido in pedidos:
        imprimir_pedido(pedido)


def registrar_pedido():
    """Solicita los datos y registra un nuevo pedido."""
    mostrar_encabezado("REGISTRAR PEDIDO")
    mostrar_clientes()
    mostrar_productos()

    pedido = Pedido(
        input("\nClave del cliente: "),
        input("Clave del producto: "),
        input("Cantidad: "),
    )

    numero = pedido.crear_pedido()
    pedido_registrado = Pedido.buscar_pedido(numero)

    print("\nPedido registrado correctamente.")
    print(f"El ticket se generó como ticket_pedido_{numero}.txt")
    imprimir_pedido(pedido_registrado)


def cancelar_pedido():
    """Solicita el número y cancela un pedido activo."""
    mostrar_encabezado("CANCELAR PEDIDO")
    mostrar_pedidos()

    numero = input("\nNúmero del pedido que deseas cancelar: ").strip()

    if Pedido.cancelar_pedido(numero):
        print("\nPedido cancelado correctamente.")
    else:
        print("\nEl pedido no existe o ya se encuentra cancelado.")


def consultar_pedido():
    """Busca y presenta un pedido mediante su número."""
    mostrar_encabezado("CONSULTAR PEDIDO")

    numero = input("Número del pedido: ").strip()
    imprimir_pedido(Pedido.buscar_pedido(numero))


def menu_pedidos():
    """Controla las operaciones disponibles para los pedidos."""
    while True:
        mostrar_encabezado("ADMINISTRACIÓN DE PEDIDOS")
        print("1. Registrar pedido")
        print("2. Cancelar pedido")
        print("3. Consultar pedido")
        print("4. Mostrar pedidos")
        print("5. Regresar")

        opcion = input("\nSelecciona una opción: ").strip()

        try:
            if opcion == "1":
                registrar_pedido()
            elif opcion == "2":
                cancelar_pedido()
            elif opcion == "3":
                consultar_pedido()
            elif opcion == "4":
                mostrar_encabezado("REGISTRO DE PEDIDOS")
                mostrar_pedidos()
            elif opcion == "5":
                return
            else:
                print("\nOpción no válida.")
        except (ValueError, sqlite3.Error) as error:
            print(f"\nNo fue posible realizar la operación: {error}")

        if opcion != "5":
            pausar()


def mostrar_menu_principal():
    """Muestra las opciones principales de Happy Burger."""
    mostrar_encabezado("HAPPY BURGER")
    print("1. Pedidos")
    print("2. Clientes")
    print("3. Menú")
    print("4. Salir")


def main():
    """Inicializa la base de datos y ejecuta la aplicación."""
    crear_tablas()

    while True:
        mostrar_menu_principal()
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "1":
            menu_pedidos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_productos()
        elif opcion == "4":
            print("\nGracias por utilizar Happy Burger. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Selecciona un número del 1 al 4.")
            pausar()


if __name__ == "__main__":
    main()