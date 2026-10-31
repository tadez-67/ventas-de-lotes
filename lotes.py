from validaciones import (
    validar_codigo_unico,
    validar_numero_positivo,
    validar_texto,
)


def registrar_lote(lotes, codigo, urbanizacion, area, precio_m2):
    lote = {
        "codigo": validar_codigo_unico(codigo, lotes),
        "urbanizacion": validar_texto(urbanizacion, "Urbanización"),
        "area": validar_numero_positivo(area, "Área"),
        "precio_m2": validar_numero_positivo(precio_m2, "Precio por m²"),
        "estado": "Disponible",
    }
    lotes.append(lote)
    return lote


def listar_lotes(lotes):
    return list(lotes)


def obtener_disponibles(lotes):
    return [lote for lote in lotes if lote["estado"] == "Disponible"]


def buscar_lote(lotes, codigo):
    codigo = str(codigo).strip().upper()
    return next((lote for lote in lotes if lote["codigo"] == codigo), None)
