PORCENTAJE_INICIAL = 0.20

def calcular_precio_total(area, precio_m2):
 return round(area * precio_m2, 2)

def calcular_cuota_inicial(total):
 return round(total * PORCENTAJE_INICIAL, 2)

def calcular_saldo(total, cuota_inicial):
 return round(total - cuota_inicial, 2)