from lotes import registrar_lote, listar_lotes, obtener_disponibles
from ventas import registrar_venta, listar_ventas

def mostrar_lotes(items):
    if not items:
        print("No hay lotes para mostrar.")
    for l in items:
        print(f'{l["codigo"]} | {l["urbanizacion"]} | '
              f'{l["area"]:.2f} m² | S/ {l["precio_m2"]:.2f} | {l["estado"]}')

def mostrar_ventas(items):
    if not items:
        print("No hay ventas registradas.")
    for v in items:
        print(f'{v["lote"]} | {v["comprador"]} | '
              f'Total S/ {v["precio_total"]:.2f} | '
              f'Inicial S/ {v["cuota_inicial"]:.2f} | Saldo S/ {v["saldo"]:.2f}')
        
def main():
    lotes, ventas = [], []
    while True:
        print("\n1. Registrar lote 2. Listar lotes 3. Disponibles")
        print("4. Vender lote 5. Resumen de ventas 6. Salir")
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                lote = registrar_lote(lotes, input("Código: "),
                    input("Urbanización: "), input("Área: "),
                    input("Precio por m²: "))
                print("Lote registrado:", lote["codigo"])
            elif opcion == "2": mostrar_lotes(listar_lotes(lotes))
            elif opcion == "3": mostrar_lotes(obtener_disponibles(lotes))
            elif opcion == "4":
                venta = registrar_venta(lotes, ventas, input("Código: "),
                    input("Comprador: "), input("Documento: "))
                print("Venta registrada. Total: S/", f'{venta["precio_total"]:.2f}')
            elif opcion == "5": mostrar_ventas(listar_ventas(ventas))
            elif opcion == "6":
                print("Sistema finalizado."); break
            else: print("Opción inválida.")
        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
