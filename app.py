"""Aplicación web para consultar pedidos de Happy Burger."""

from flask import Flask, render_template, request

from database import crear_tablas
from modelos import Pedido


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def consultar_pedido():
    """Consulta un pedido por número y muestra el resultado."""
    pedido = None
    mensaje = None
    numero = ""

    if request.method == "POST":
        numero = request.form.get("numero", "").strip()

        if not numero:
            mensaje = "Ingresa un número de pedido."
        else:
            try:
                pedido = Pedido.buscar_pedido(numero)
            except ValueError as error:
                mensaje = str(error)
            else:
                if pedido is None:
                    mensaje = "No se encontró un pedido con ese número."

    return render_template(
        "buscar_pedido.html",
        pedido=pedido,
        mensaje=mensaje,
        numero=numero,
    )


if __name__ == "__main__":
    crear_tablas()
    app.run(debug=True)