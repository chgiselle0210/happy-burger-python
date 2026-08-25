"""Módulo que define la entidad y las operaciones de los clientes."""

import sqlite3

from database import obtener_conexion
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
        """Guarda al cliente actual en la base de datos."""
        try:
            with obtener_conexion() as conexion:
                conexion.execute(
                    """
                    INSERT INTO clientes (
                        clave,
                        nombre,
                        direccion,
                        correo_electronico,
                        telefono
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        self.clave,
                        self.nombre,
                        self.direccion,
                        self.correo_electronico,
                        self.telefono,
                    ),
                )
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "La clave o el correo electrónico ya están registrados."
            ) from error

        return True

    @staticmethod
    def eliminar_cliente(clave):
        """Elimina un cliente mediante su clave."""
        clave = Cliente.validar_cadena(clave, "clave")

        with obtener_conexion() as conexion:
            cursor = conexion.execute(
                "DELETE FROM clientes WHERE clave = ?",
                (clave,),
            )

        return cursor.rowcount > 0

    def actualizar_cliente(self):
        """Actualiza todos los datos del cliente identificado por su clave."""
        try:
            with obtener_conexion() as conexion:
                cursor = conexion.execute(
                    """
                    UPDATE clientes
                    SET nombre = ?,
                        direccion = ?,
                        correo_electronico = ?,
                        telefono = ?
                    WHERE clave = ?
                    """,
                    (
                        self.nombre,
                        self.direccion,
                        self.correo_electronico,
                        self.telefono,
                        self.clave,
                    ),
                )
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "El correo electrónico ya pertenece a otro cliente."
            ) from error

        return cursor.rowcount > 0

    @staticmethod
    def buscar_cliente(clave):
        """Busca un cliente mediante su clave."""
        clave = Cliente.validar_cadena(clave, "clave")

        with obtener_conexion() as conexion:
            fila = conexion.execute(
                "SELECT * FROM clientes WHERE clave = ?",
                (clave,),
            ).fetchone()

        return dict(fila) if fila else None

    @staticmethod
    def listar_clientes():
        """Devuelve todos los clientes ordenados por nombre."""
        with obtener_conexion() as conexion:
            filas = conexion.execute(
                "SELECT * FROM clientes ORDER BY nombre"
            ).fetchall()

        return [dict(fila) for fila in filas]