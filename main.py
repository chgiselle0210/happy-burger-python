"""Aplicación principal de consola para el sistema Happy Burger."""


def mostrar_menu_principal():
    """Muestra las opciones principales disponibles en el sistema."""
    print("\n" + "=" * 45)
    print("           HAPPY BURGER")
    print("=" * 45)
    print("1. Pedidos")
    print("2. Clientes")
    print("3. Menú")
    print("4. Salir")
    print("=" * 45)


def calcular_pedido():
    """Solicita un producto y calcula el total según su precio y cantidad."""
    print("\n--- Registro provisional de pedido ---")

    nombre_producto = input("Nombre del producto: ").strip()

    if not nombre_producto:
        print("El nombre del producto no puede quedar vacío.")
        return

    try:
        precio = float(input("Precio del producto: $"))
        cantidad = int(input("Cantidad solicitada: "))

        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben ser mayores que cero.")
            return

        total = precio * cantidad

        print("\n--- Resumen del pedido ---")
        print(f"Producto: {nombre_producto}")
        print(f"Precio unitario: ${precio:.2f}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: ${total:.2f}")

    except ValueError:
        print("El precio y la cantidad deben ingresarse con valores numéricos.")


def procesar_opcion(opcion):
    """Controla el flujo del programa según la opción seleccionada."""
    if opcion == "1":
        calcular_pedido()
    elif opcion == "2":
        print("\nSeleccionaste la opción Clientes.")
        print("Este módulo se integrará en el siguiente avance.")
    elif opcion == "3":
        print("\nSeleccionaste la opción Menú.")
        print("Este módulo se integrará en el siguiente avance.")
    elif opcion == "4":
        print("\nGracias por utilizar Happy Burger. ¡Hasta pronto!")
        return False
    else:
        print("\nOpción no válida. Selecciona un número del 1 al 4.")

    return True


def main():
    """Ejecuta el menú principal hasta que el usuario decida salir."""
    continuar = True

    while continuar:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ").strip()
        continuar = procesar_opcion(opcion)


if __name__ == "__main__":
    main()