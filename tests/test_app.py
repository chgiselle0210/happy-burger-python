"""Pruebas para la consulta web desarrollada con Flask."""

from app import app
from modelos import Cliente, Menu, Pedido


def preparar_pedido():
    """Registra datos para consultar un pedido desde Flask."""
    Cliente(
        "C001",
        "Ana López",
        "Av. Central 100",
        "ana@example.com",
        "6141234567",
    ).agregar_cliente()

    Menu(
        "P001",
        "Hamburguesa clásica",
        85.50,
    ).agregar_producto()

    return Pedido("C001", "P001", 2).crear_pedido()


def test_consulta_web_de_pedido():
    """Comprueba que Flask muestre un pedido existente."""
    numero = preparar_pedido()
    app.config["TESTING"] = True

    with app.test_client() as cliente_web:
        respuesta = cliente_web.post(
            "/",
            data={"numero": str(numero)},
        )

    contenido = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "Ana López" in contenido
    assert "Hamburguesa clásica" in contenido
    assert "$171.00" in contenido
    assert "ACTIVO" in contenido


def test_consulta_web_inexistente():
    """Comprueba el mensaje para un pedido que no existe."""
    app.config["TESTING"] = True

    with app.test_client() as cliente_web:
        respuesta = cliente_web.post(
            "/",
            data={"numero": "999"},
        )

    contenido = respuesta.get_data(as_text=True)

    assert respuesta.status_code == 200
    assert "No se encontró un pedido con ese número." in contenido