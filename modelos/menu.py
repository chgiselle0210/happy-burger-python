"""Módulo que define los productos disponibles en el menú."""

import sqlite3

from database import obtener_conexion
from modelos.entidad_base import EntidadBase


class Menu(EntidadBase):
    """Representa un producto registrado en el menú de Happy Burger."""

    def __init__(self, clave, nombre, precio):
        """Inicializa un producto con su clave, nombre y precio."""
        self.clave = self.validar_cadena(clave, "clave")
        self.nombre = self.validar_cadena(nombre, "nombre")

        try:
            self.precio = float(precio)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser un valor numérico.") from error

        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

    def agregar_producto(self):
        """Guarda el producto actual en la base de datos."""
        try:
            with obtener_conexion() as conexion:
                conexion.execute(
                    """
                    INSERT INTO menu (clave, nombre, precio)
                    VALUES (?, ?, ?)
                    """,
                    (
                        self.clave,
                        self.nombre,
                        self.precio,
                    ),
                )
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Ya existe un producto registrado con esa clave."
            ) from error

        return True

    @staticmethod
    def eliminar_producto(clave):
        """Elimina un producto mediante su clave."""
        clave = Menu.validar_cadena(clave, "clave")

        with obtener_conexion() as conexion:
            cursor = conexion.execute(
                "DELETE FROM menu WHERE clave = ?",
                (clave,),
            )

        return cursor.rowcount > 0

    def actualizar_producto(self):
        """Actualiza el nombre y precio del producto actual."""
        with obtener_conexion() as conexion:
            cursor = conexion.execute(
                """
                UPDATE menu
                SET nombre = ?, precio = ?
                WHERE clave = ?
                """,
                (
                    self.nombre,
                    self.precio,
                    self.clave,
                ),
            )

        return cursor.rowcount > 0

    @staticmethod
    def buscar_producto(clave):
        """Busca un producto mediante su clave."""
        clave = Menu.validar_cadena(clave, "clave")

        with obtener_conexion() as conexion:
            fila = conexion.execute(
                "SELECT * FROM menu WHERE clave = ?",
                (clave,),
            ).fetchone()

        return dict(fila) if fila else None

    @staticmethod
    def listar_productos():
        """Devuelve todos los productos ordenados por nombre."""
        with obtener_conexion() as conexion:
            filas = conexion.execute(
                "SELECT * FROM menu ORDER BY nombre"
            ).fetchall()

        return [dict(fila) for fila in filas]