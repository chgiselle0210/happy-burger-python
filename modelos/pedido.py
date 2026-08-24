"""Módulo que define la entidad y las operaciones de los pedidos."""

from modelos.entidad_base import EntidadBase


class Pedido(EntidadBase):
    """Representa un pedido realizado en Happy Burger."""

    def __init__(self, pedido, cliente, producto, precio):
        """Inicializa un pedido con los campos solicitados en el proyecto."""
        if not isinstance(pedido, int) or pedido <= 0:
            raise ValueError("El número de pedido debe ser un entero positivo.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.pedido = pedido
        self.cliente = self.validar_cadena(cliente, "cliente")
        self.producto = self.validar_cadena(producto, "producto")
        self.precio = float(precio)

    def crear_pedido(self):
        """Registra un nuevo pedido en el sistema."""
        pass

    def cancelar_pedido(self):
        """Cancela un pedido existente."""
        pass