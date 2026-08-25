"""Pruebas de clientes, productos, pedidos y tickets."""

from modelos import Cliente, Menu, Pedido


def crear_datos_base():
    """Crea un cliente y un producto para las pruebas de pedidos."""
    cliente = Cliente(
        "C001",
        "Ana López",
        "Av. Central 100",
        "ana@example.com",
        "6141234567",
    )
    producto = Menu(
        "P001",
        "Hamburguesa clásica",
        85.50,
    )

    cliente.agregar_cliente()
    producto.agregar_producto()


def test_operaciones_cliente():
    """Comprueba alta, consulta, actualización y eliminación."""
    cliente = Cliente(
        "C001",
        "Ana López",
        "Av. Central 100",
        "ana@example.com",
        "6141234567",
    )

    assert cliente.agregar_cliente() is True
    assert Cliente.buscar_cliente("C001")["nombre"] == "Ana López"

    actualizado = Cliente(
        "C001",
        "Ana López García",
        "Av. Central 200",
        "ana.lopez@example.com",
        "6147654321",
    )

    assert actualizado.actualizar_cliente() is True
    assert (
        Cliente.buscar_cliente("C001")["nombre"]
        == "Ana López García"
    )

    assert Cliente.eliminar_cliente("C001") is True
    assert Cliente.buscar_cliente("C001") is None


def test_operaciones_producto():
    """Comprueba alta, consulta, actualización y eliminación."""
    producto = Menu(
        "P001",
        "Hamburguesa clásica",
        85.50,
    )

    assert producto.agregar_producto() is True
    assert Menu.buscar_producto("P001")["precio"] == 85.50

    actualizado = Menu(
        "P001",
        "Hamburguesa especial",
        89.50,
    )

    assert actualizado.actualizar_producto() is True
    assert Menu.buscar_producto("P001")["precio"] == 89.50

    assert Menu.eliminar_producto("P001") is True
    assert Menu.buscar_producto("P001") is None


def test_registro_de_pedido_y_ticket(entorno_pruebas):
    """Comprueba el registro, cálculo y generación del ticket."""
    crear_datos_base()

    pedido = Pedido("C001", "P001", 2)
    numero = pedido.crear_pedido()
    registro = Pedido.buscar_pedido(numero)

    assert registro["cliente"] == "Ana López"
    assert registro["producto"] == "Hamburguesa clásica"
    assert registro["cantidad"] == 2
    assert registro["total"] == 171.00
    assert registro["estado"] == "ACTIVO"

    ruta_ticket = (
        entorno_pruebas["tickets"]
        / f"ticket_pedido_{numero}.txt"
    )

    assert ruta_ticket.exists()

    contenido = ruta_ticket.read_text(encoding="utf-8")

    assert "Ana López" in contenido
    assert "Total: $171.00" in contenido


def test_cancelacion_de_pedido():
    """Comprueba que un pedido activo pueda cancelarse."""
    crear_datos_base()

    pedido = Pedido("C001", "P001", 1)
    numero = pedido.crear_pedido()

    assert Pedido.cancelar_pedido(numero) is True
    assert Pedido.buscar_pedido(numero)["estado"] == "CANCELADO"
    assert Pedido.cancelar_pedido(numero) is False