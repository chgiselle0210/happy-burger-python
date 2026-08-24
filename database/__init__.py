"""Herramientas de persistencia de datos para Happy Burger."""

from database.conexion import RUTA_BASE_DATOS, crear_tablas, obtener_conexion

__all__ = ["RUTA_BASE_DATOS", "crear_tablas", "obtener_conexion"]