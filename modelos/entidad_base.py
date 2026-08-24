"""Clase base para las entidades administrativas de Happy Burger."""


class EntidadBase:
    """Proporciona comportamientos comunes para las entidades del sistema."""

    @staticmethod
    def validar_cadena(valor, nombre_campo):
        """Valida que un dato sea una cadena de texto con contenido."""
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El campo {nombre_campo} no puede quedar vacío.")

        return valor.strip()

    def a_diccionario(self):
        """Devuelve los atributos de la instancia como un diccionario."""
        return self.__dict__.copy()