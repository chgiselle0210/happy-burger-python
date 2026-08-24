"""Módulo que define los productos disponibles en el menú."""

from modelos.entidad_base import EntidadBase


class Menu(EntidadBase):
    """Representa un producto registrado en el menú de Happy Burger."""

    def __init__(self, clave, nombre, precio):
        """Inicializa un producto con su clave, nombre y precio."""
        self.clave = self.validar_cadena(clave, "clave")
        self.nombre = self.validar_cadena(nombre, "nombre")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.precio = float(precio)

    def agregar_producto(self):
        """Agrega un producto al menú."""
        pass

    def eliminar_producto(self):
        """Elimina un producto del menú."""
        pass

    def actualizar_producto(self):
        """Actualiza los datos de un producto existente."""
        pass