"""

"""
import os 

cuentasBancarias = {}

def limpiarConsola():
    limpiar = os.system("cls" if os.name == "nt" else "clear")
    return limpiar

def menuPrincipal():
    print('1.Crear cuenta \n2. Depositar dinero \n3. Solicitar Credito \n4. Retirar dinero \n5. Pago cuota credito \n6. Cancelar cuenta \n0. salir ')

def agregarCuenta(numeroCuenta, nombre, cc, correo, edad, movil, fijo, pais, dep, ciudad, direccion,idProducto, producto, estado):
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
        