"""Configuración compartida para las pruebas de Happy Burger."""

import pytest

from database import conexion, crear_tablas
from servicios import ticket_service


@pytest.fixture(autouse=True)
def entorno_pruebas(tmp_path, monkeypatch):
    """Utiliza una base y un directorio de tickets temporales."""
    ruta_base_datos = tmp_path / "happy_burger_pruebas.db"
    ruta_tickets = tmp_path / "tickets"

    monkeypatch.setattr(
        conexion,
        "RUTA_BASE_DATOS",
        ruta_base_datos,
    )
    monkeypatch.setattr(
        ticket_service,
        "DIRECTORIO_TICKETS",
        ruta_tickets,
    )

    crear_tablas()

    return {
        "base_datos": ruta_base_datos,
        "tickets": ruta_tickets,
    }