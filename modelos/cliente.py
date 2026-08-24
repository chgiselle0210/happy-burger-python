"""Módulo que define la entidad y las operaciones de los clientes."""

from modelos.entidad_base import EntidadBase


class Cliente(EntidadBase):
    """Representa a un cliente registrado en Happy Burger."""

    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        """Inicializa un cliente con los campos solicitados en el proyecto."""
        self.clave = self.validar_cadena(clave, "clave")
        self.nombre = self.validar_cadena(nombre, "nombre")
        self.direccion = self.validar_cadena(direccion, "dirección")
        self.correo_electronico = self.validar_cadena(
            correo_electronico,
            "correo electrónico",
        )
        self.telefono = self.validar_cadena(telefono, "teléfono")

    def agregar_cliente(self):
        """Agrega un cliente al sistema."""
        pass

    def eliminar_cliente(self):
        """Elimina un cliente del sistema."""
        pass

    def actualizar_cliente(self):
        """Actualiza los datos de un cliente existente."""
        pass