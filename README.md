SISTEMA DE VENTA DE LOTES

Descripción:
Este proyecto implementa un sistema modular en Python para gestionar el registro y la venta de lotes de la empresa Terrenos del Norte S.A.C.
El sistema permite registrar lotes, consultar su disponibilidad, registrar compradores, calcular el precio total de una venta, determinar la cuota inicial y calcular el saldo pendiente.

Objetivo:
Desarrollar una solución aplicando los principios de programación modular, separación de responsabilidades y reutilización de funciones.

Funcionalidades:
-Registrar lotes.
-Validar códigos de lote duplicados.
-Validar campos vacíos.
-Validar que el área y el precio sean mayores que cero.
-Mostrar todos los lotes registrados.
-Consultar lotes disponibles.
-Registrar la venta de un lote.
-Calcular el precio total.
-Calcular la cuota inicial del 20 %.
-Calcular el saldo pendiente.
-Cambiar el estado del lote de Disponible a Vendido.
-Evitar que un lote sea vendido dos veces.
-Mostrar un resumen de las ventas.

Estructura del proyecto:
-main.py: contiene el menú y coordina el funcionamiento del sistema.
-lotes.py: administra el registro, búsqueda y disponibilidad de los lotes.
-ventas.py: registra las ventas y cambia el estado de los lotes.
-calculos.py: calcula el precio total, la cuota inicial y el saldo.
-validaciones.py: comprueba los datos ingresados por el usuario.

Requisitos:

Python

No requiere instalar librerías externas.

Instrucciones de ejecución:
1-Descargar o clonar el repositorio.
2-brir una terminal dentro de la carpeta del proyecto.
3-Ejecutar el siguiente comando:
python main.py

Datos utilizados en las pruebas:

Lote LT-001
-Urbanización: Los Jardines
-Área: 120 m²
-Precio por m²: S/ 450.00
-Precio total: S/ 54 000.00
-Cuota inicial: S/ 10 800.00
-Saldo pendiente: S/ 43 200.00

Lote LT-002
-Urbanización: Las Palmeras
-Área: 90 m²
-Precio por m²: S/ 500.00
-Precio total: S/ 45 000.00
-Cuota inicial: S/ 9 000.00
-Saldo pendiente: S/ 36 000.00

Casos de prueba:

El sistema fue probado con los siguientes casos:

-Registro correcto de lotes.
-Intento de registrar un código duplicado.
-Ingreso de áreas negativas o iguales a cero.
-Ingreso de campos vacíos.
-Venta de un lote disponible.
-Intento de vender un lote inexistente.
-Intento de vender dos veces el mismo lote.
-Verificación del precio total, cuota inicial y saldo.

Integrantes:
Alegre Pereira, Jhoel Harold – N00410114
Zavaleta Abanto, Piero Alessando - N00547287
Castañeda Alcántara, Hummer Sthif – N00529991
Tapia Fernández, Angel Daniel – N00543132
Martínez Guevara, Diego – N00554012

Curso:
Fundamentos De Programación

Estado del proyecto:
Proyecto académico completado y disponible para evaluación.
