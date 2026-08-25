"""Módulo que administra los pedidos de Happy Burger."""

from database import obtener_conexion
from modelos.entidad_base import EntidadBase
from servicios import generar_ticket


class Pedido(EntidadBase):
    """Representa un pedido asociado con un cliente y un producto."""

    def __init__(self, cliente_clave, producto_clave, cantidad=1):
        """Inicializa los datos necesarios para registrar un pedido."""
        self.cliente_clave = self.validar_cadena(
            cliente_clave,
            "clave del cliente",
        )
        self.producto_clave = self.validar_cadena(
            producto_clave,
            "clave del producto",
        )

        try:
            self.cantidad = int(cantidad)
        except (TypeError, ValueError) as error:
            raise ValueError(
                "La cantidad debe ser un número entero."
            ) from error

        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.pedido = None
        self.cliente = None
        self.producto = None
        self.precio = None
        self.total = None

    def crear_pedido(self):
        """Consulta cliente y producto, registra el pedido y genera su ticket."""
        with obtener_conexion() as conexion:
            cliente = conexion.execute(
                "SELECT * FROM clientes WHERE clave = ?",
                (self.cliente_clave,),
            ).fetchone()

            if cliente is None:
                raise ValueError("No existe un cliente con esa clave.")

            producto = conexion.execute(
                "SELECT * FROM menu WHERE clave = ?",
                (self.producto_clave,),
            ).fetchone()

            if producto is None:
                raise ValueError("No existe un producto con esa clave.")

            self.cliente = cliente["nombre"]
            self.producto = producto["nombre"]
            self.precio = float(producto["precio"])
            self.total = self.precio * self.cantidad

            cursor = conexion.execute(
                """
                INSERT INTO pedidos (
                    cliente_clave,
                    producto_clave,
                    cliente,
                    producto,
                    precio,
                    cantidad,
                    total
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    self.cliente_clave,
                    self.producto_clave,
                    self.cliente,
                    self.producto,
                    self.precio,
                    self.cantidad,
                    self.total,
                ),
            )

            self.pedido = cursor.lastrowid

        datos_pedido = self.buscar_pedido(self.pedido)
        generar_ticket(datos_pedido)

        return self.pedido

    @staticmethod
    def cancelar_pedido(numero_pedido):
        """Cambia el estado de un pedido existente a CANCELADO."""
        try:
            numero_pedido = int(numero_pedido)
        except (TypeError, ValueError) as error:
            raise ValueError(
                "El número de pedido debe ser un entero."
            ) from error

        with obtener_conexion() as conexion:
            cursor = conexion.execute(
                """
                UPDATE pedidos
                SET estado = 'CANCELADO'
                WHERE pedido = ? AND estado = 'ACTIVO'
                """,
                (numero_pedido,),
            )

        return cursor.rowcount > 0

    @staticmethod
    def buscar_pedido(numero_pedido):
        """Busca y devuelve un pedido mediante su número."""
        try:
            numero_pedido = int(numero_pedido)
        except (TypeError, ValueError) as error:
            raise ValueError(
                "El número de pedido debe ser un entero."
            ) from error

        with obtener_conexion() as conexion:
            fila = conexion.execute(
                "SELECT * FROM pedidos WHERE pedido = ?",
                (numero_pedido,),
            ).fetchone()

        return dict(fila) if fila else None

    @staticmethod
    def listar_pedidos():
        """Devuelve todos los pedidos del más reciente al más antiguo."""
        with obtener_conexion() as conexion:
            filas = conexion.execute(
                "SELECT * FROM pedidos ORDER BY pedido DESC"
            ).fetchall()

        return [dict(fila) for fila in filas]