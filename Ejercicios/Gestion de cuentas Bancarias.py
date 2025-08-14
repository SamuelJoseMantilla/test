"""
Autor: Samuel José Mantilla Pallares.
Fecha: 13/08/2025
Descripcion: Este es un programa de gestion de cuentas bancarias que puede agregar y retirar fondos, pedir y cancelar creditos y eliminar cuentas
"""
import os, random, time

cuentasBancarias = {}

def limpiarConsola():
    limpiar = os.system("cls" if os.name == "nt" else "clear")
    return limpiar

def menuPrincipal():
    print('1. Crear cuenta \n2. Depositar dinero \n3. Solicitar Credito \n4. Retirar dinero \n5. Pago cuota credito \n6. Cancelar cuenta \n0. salir ')

def datosClientes(numeroCuenta, nombre, cc, correo, edad, movil, fijo, pais, dep, ciudad, direccion,idProducto, producto, estado):
    if numeroCuenta in cuentasBancarias:
        print('La cuenta ya existe.')
    else:
        cuentasBancarias[numeroCuenta] = {   "CC": cc,
            "titular": nombre,
            "Correo": correo,
            "Edad": edad,
            "Contacto": {
                "Movil": movil,
                "Fijo": fijo
            },
            "Ubicacion": {
                "Pais": pais,
                "Departamento": dep,
                "Ciudad": ciudad,
                "Direccion": direccion
            },
            "Productos": {
                idProducto: {
                    'NombreProducto' : producto,
                    'Saldo': 0,
                    'Estado': estado,
                    'Historial' : {}
                }
            },
        }

def saldos():
    print('1. Cta Ahorros \n2. Cta Corriente')

def solicitarCredito():
    print('1. Credito Libre Inversion \n2. Credito Vivienda \n3. Credito Compra AutoMovil \n0. Salir ')

def agregarHistorial(numeroCuenta, idProducto, valor, tipoMovimiento):
    """Registra un movimiento en el historial de un producto."""
    if numeroCuenta in cuentasBancarias and idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
        historial = cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Historial"]

        nuevo_id = len(historial) + 1
        historial[nuevo_id] = {
            "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Valor": valor,
            "TipoMovimiento": tipoMovimiento
        }
    else:
        print("No se pudo registrar el historial: cuenta o producto no encontrado.")


def portafolio():
    print('1. Cta Ahorros \n2. Cta Corriente \n3. CDT \n0. Salir')

numeroCuenta = 1000
ctaCorriente = 1000
ctaAhorros = 800
cdt = 9000
creditoLibreInv = 10000
creditoVivienda = 50000
creditoCompraAuto = 40000
producto = ''

while True:
    try:
        menuPrincipal()
        opcion = int(input('Ingresa una Opcion: '))
        match opcion:
            case 1:
                limpiarConsola()

                while True:
                    try:
                        portafolio()
                        opcion = input('Ingrese una opcion valida: ')
                        e = True
                        idProducto = None

                        match opcion:
                            case "1":
                                producto = "Cuenta de Ahorros"
                                while e:
                                    idProducto = random.randint(100, ctaAhorros)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break
                            case "2":
                                producto = "Cuenta Corriente"
                                while e:
                                    idProducto = random.randint(400, ctaCorriente)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break
                            case "3":
                                producto = "CDT"
                                while e:
                                    idProducto = random.randint(5000, ctaCorriente)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False

                                monto_inversion = float(input("Ingrese el monto a invertir en el CDT: "))
                                plazo_dias = int(input("Ingrese el plazo del CDT (en días): "))
                                tasa_interes = 0.05

                                datos_cdt = {
                                    "monto": monto_inversion,
                                    "plazo": plazo_dias,
                                    "tasa": tasa_interes
                                }
                                break
                            case "0":
                                print("Cancelando creación de cuenta...")
                                break
                            case _:
                                print('Ingresa una Opcion valida')
                                continue
                    except (ValueError,KeyboardInterrupt,TypeError) as e:
                        print(f'Error: {e}')

                if idProducto is None:
                    continue

                limpiarConsola()
                print("Crear Cuenta")

                numeroCuenta = random.randint(1, numeroCuenta)
                print(f'Tu numero de cuenta general es: {numeroCuenta}')
                print(f'Tu producto: {producto}, el numero es: {idProducto}')

                cc = input('Ingresa la cedula del titular: ')
                titular = input("Ingrese el nombre del titular: ")
                email = input('Ingresa el correo del titular: ')
                edad = int(input('Ingresa la edad del titular: '))

                print('Ingresa el movil y fijo del titular: ')
                movil = int(input('Ingresa el movil del titular: '))
                fijo = int(input('Ingresa el fijo del titular: '))

                print('Ingresa los datos de residencia del titular: ')
                pais = input('Ingresa el pais del titular: ')
                dep = input('Ingresa el departamento del titular: ')
                ciudad = input('Ingresa la ciudad del titular: ')
                direccion = input('Ingresa la Direccion del titular: ')

                estado = "Activo"
                datosClientes(numeroCuenta, titular, cc, email, edad, movil, fijo, pais, dep, ciudad, direccion,idProducto, producto, estado)

                if producto == "CDT":
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Saldo"] = datos_cdt["monto"]
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Plazo"] = datos_cdt["plazo"]
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Tasa"] = datos_cdt["tasa"]
                    agregarHistorial(numeroCuenta, idProducto, datos_cdt["monto"], "Apertura CDT")

                input("Presione Enter para continuar...")
                limpiarConsola()
            case 2:

                limpiarConsola()
                print("Depositar Dinero")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:

                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    idProducto = int(input("\nIngrese el ID del producto al que desea depositar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        monto = float(input("Ingrese el monto a depositar: "))

                        cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] += monto
                        agregarHistorial(numeroCuenta, idProducto, monto, "Depósito")

                        print(f"\nDepósito realizado con éxito.")
                        print(f"Nuevo saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")
                    else:
                        print("El producto no existe.")
                else:
                    print(f'La cuenta {numeroCuenta} No esta asociada')

                input("\nPresione Enter para continuar...")
                limpiarConsola()

            case 3:

                limpiarConsola()
                print('=== Solicitar Crédito ===')

                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta not in cuentasBancarias:
                    print("La cuenta no existe.")
                    input("Enter para continuar...")
                    break

                while True:
                    try:
                        print('\n¿Qué tipo de crédito deseas solicitar?')
                        opcion = input('1. Crédito Libre Inversión \n2. Crédito Vivienda \n3. Crédito Compra Automóvil \n0. Salir \nOpción: ')
                        e = True
                        idProducto = None

                        match opcion:
                            case "1":
                                producto = 'Crédito Libre Inversión'
                                while e:
                                    idProducto = random.randint(8000, creditoLibreInv)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "2":
                                producto = 'Crédito Vivienda'
                                while e:
                                    idProducto = random.randint(4000, creditoVivienda)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "3":
                                producto = 'Crédito Compra Automóvil'
                                while e:
                                    idProducto = random.randint(10000, creditoCompraAuto)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "0":
                                print("Solicitud cancelada.")
                                continue
                            case _:
                                print("Opción inválida.")
                                continue
                    except (ValueError, KeyboardInterrupt, TypeError) as e:
                        print(f'Error: {e}')

                limpiarConsola()

                ingresosMensuales = float(input('Ingresa el total de ingresos mensuales: '))
                montoSolicitado = float(input('Ingresa el monto de crédito solicitado: '))
                plazoMeses = int(input('Ingresa el plazo (meses) para pagar: '))
                limpiarConsola()

                cuota = montoSolicitado / plazoMeses
                RCI = cuota / ingresosMensuales

                print(f"\nEvaluando crédito... (RCI: {RCI:.2f})")
                time.sleep(1)

                limpiarConsola()

                if RCI <= 0.4:
                    print(" Crédito aprobado.")

                    cuentasBancarias[numeroCuenta]["Productos"][idProducto] = {
                        "NombreProducto": producto,
                        "TipoProducto": "credito",
                        "Saldo": montoSolicitado,
                        "Estado": "Activo",
                        "Historial": {
                            1: {
                                "FechaMovimiento": time.strftime("%Y-%m-%d"),
                                "Valor": montoSolicitado,
                                "TipoMovimiento": "Crédito Aprobado"
                            }
                        }
                    }
                    print(f"Crédito {producto} creado con ID {idProducto} y saldo {montoSolicitado}")
                else:
                    print(" No eres apto para el crédito (RCI mayor a 0.4).")
                input("Enter para continuar...")
                limpiarConsola()

            case 4:

                limpiarConsola()
                print("Retirar Dinero")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:

                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    idProducto = int(input("\nIngrese el ID del producto al que desea Retirar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        monto = float(input("Ingrese el monto a Retirar: "))

                        if cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] >= monto:
                            cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] -= monto
                            agregarHistorial(numeroCuenta, idProducto, -monto, "Retiro")

                            print(f"\nDepósito realizado con éxito.")
                            print(f"Nuevo saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")
                        else:
                            print('Saldo insuficiente')
                            print(f"Saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")

                    else:
                        print("El producto no existe.")
                else:
                    print("La cuenta no existe.")

                input("\nPresione Enter para continuar...")
                limpiarConsola()

            case 5:
                #Pago de la cuota del Credito
                limpiarConsola()
                print("Pago de Cuota de Crédito")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:
                    # Mostrar productos disponibles
                    print("Productos de la cuenta:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"ID: {idProd} - {datosProd['NombreProducto']} - Saldo: {datosProd['Saldo']} - Estado: {datosProd['Estado']}")

                    idProducto = int(input("Ingrese el ID del producto (crédito) a pagar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        producto = cuentasBancarias[numeroCuenta]["Productos"][idProducto]

                        if producto["TipoProducto"] == "credito":
                            monto = float(input("Ingrese el monto a pagar: "))

                            if monto > 0:
                                if monto >= producto["Saldo"]:
                                    producto["Saldo"] -= monto
                                    agregarHistorial(numeroCuenta, idProducto, -monto, "Pago Cuota Crédito")

                                    print("Crédito pagado en su totalidad.")
                                else:
                                    producto["Saldo"] -= monto
                                    print(f"Pago realizado. Saldo restante del crédito: {producto['Saldo']}")
                            else:
                                print("El monto debe ser mayor a 0.")
                        else:
                            print("El producto seleccionado no es un crédito.")
                    else:
                        print("El ID del producto no existe.")
                else:
                    print("La cuenta no existe.")

                input("Presione Enter para continuar...")
                limpiarConsola()

            case 6:

                limpiarConsola()
                print('Cancelar Cuenta')
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:
                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    idProducto = int(input("\nIngrese el ID del producto al que desea Cancelar: "))
                    if cuentasBancarias[numeroCuenta]["Productos"][idProducto] == 0:
                        valorEliminado = cuentasBancarias[numeroCuenta]["Productos"].pop(idProducto)
                        print(valorEliminado)
                        print(cuentasBancarias)
                        print('Cuenta eliminada')
                    else:
                        print('')

                    input('Enter para continuar')

                limpiarConsola()

            case 0:
                limpiarConsola()
                print("Saliendo del sistema...")
                break

            case _:
                print('Ingresa una Opcion valida')
                limpiarConsola()

    except (ValueError,KeyboardInterrupt,TypeError) as e:
        print(f'Error {e}')
        continue


