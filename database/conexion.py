"""Conexión y configuración de la base de datos SQLite de Happy Burger."""

import sqlite3
from pathlib import Path


RUTA_BASE_DATOS = Path(__file__).resolve().parent / "happy_burger.db"


def obtener_conexion():
    """Crea y devuelve una conexión configurada con la base de datos."""
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")

    return conexion


def crear_tablas():
    """Crea las tablas necesarias si todavía no existen."""
    with obtener_conexion() as conexion:
        conexion.executescript(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                correo_electronico TEXT NOT NULL UNIQUE,
                telefono TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS menu (
                clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL CHECK (precio > 0)
            );

            CREATE TABLE IF NOT EXISTS pedidos (
                pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_clave TEXT NOT NULL,
                producto_clave TEXT NOT NULL,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                precio REAL NOT NULL CHECK (precio > 0),
                cantidad INTEGER NOT NULL CHECK (cantidad > 0),
                total REAL NOT NULL CHECK (total > 0),
                estado TEXT NOT NULL DEFAULT 'ACTIVO',
                fecha_creacion TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (cliente_clave) REFERENCES clientes (clave),
                FOREIGN KEY (producto_clave) REFERENCES menu (clave)
            );
            """
        )