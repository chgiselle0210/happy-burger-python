"""Servicio para generar tickets de consumo en archivos de texto."""

from pathlib import Path


DIRECTORIO_TICKETS = Path(__file__).resolve().parent.parent / "tickets"


def generar_ticket(datos_pedido):
    """Genera y devuelve la ruta del ticket correspondiente a un pedido."""
    DIRECTORIO_TICKETS.mkdir(exist_ok=True)

    ruta_ticket = (
        DIRECTORIO_TICKETS
        / f"ticket_pedido_{datos_pedido['pedido']}.txt"
    )

    contenido = (
        "========================================\n"
        "             HAPPY BURGER\n"
        "========================================\n"
        f"Pedido: {datos_pedido['pedido']}\n"
        f"Fecha: {datos_pedido['fecha_creacion']}\n"
        f"Cliente: {datos_pedido['cliente']}\n"
        "----------------------------------------\n"
        f"Producto: {datos_pedido['producto']}\n"
        f"Precio unitario: ${datos_pedido['precio']:.2f}\n"
        f"Cantidad: {datos_pedido['cantidad']}\n"
        "----------------------------------------\n"
        f"Total: ${datos_pedido['total']:.2f}\n"
        f"Estado: {datos_pedido['estado']}\n"
        "========================================\n"
        "        Gracias por su compra\n"
        "========================================\n"
    )

    ruta_ticket.write_text(contenido, encoding="utf-8")

    return ruta_ticket