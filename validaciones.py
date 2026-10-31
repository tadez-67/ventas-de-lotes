def validar_texto(valor, nombre_campo):
  if valor is None or not str(valor).strip():
    raise ValueError(f"{nombre_campo} no puede estar vacío.")
  return str(valor).strip()

def validar_numero_positivo(valor, nombre_campo):
 try:
   numero = float(valor)
 except (TypeError, ValueError):
   raise ValueError(f"{nombre_campo} debe ser numérico.")
 if numero <= 0:
   raise ValueError(f"{nombre_campo} debe ser mayor que cero.")
 return numero

def validar_codigo_unico(codigo, lotes):
  codigo = validar_texto(codigo, "Código").upper()
  if any(lote["codigo"] == codigo for lote in lotes):
    raise ValueError(f"El código {codigo} ya está registrado.")
  return codigo