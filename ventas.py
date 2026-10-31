from calculos import (
    calcular_precio_total,
    calcular_cuota_inicial,
    calcular_saldo,
)
from lotes import buscar_lote
from validaciones import validar_texto


def registrar_venta(lotes, ventas, codigo_lote, nombre, documento):
    lote = buscar_lote(lotes, codigo_lote)
    if lote is None:
        raise ValueError("El lote solicitado no existe.")
    if lote["estado"] != "Disponible":
        raise ValueError(
            "El lote ya fue vendido y no puede venderse otra vez."
        )
    comprador = validar_texto(nombre, "Nombre del comprador")
    documento = validar_texto(documento, "Documento de identidad")
    total = calcular_precio_total(lote["area"], lote["precio_m2"])
    inicial = calcular_cuota_inicial(total)
    saldo = calcular_saldo(total, inicial)
    venta = {
        "lote": lote["codigo"],
        "comprador": comprador,
        "documento": documento,
        "precio_total": total,
        "cuota_inicial": inicial,
        "saldo": saldo,
    }
    ventas.append(venta)
    lote["estado"] = "Vendido"
    return venta


def listar_ventas(ventas):
    return list(ventas)
