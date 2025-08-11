"""
Autor: David Andrés Gómez Castro
Fecha: 04 agosto 2025
Descripción: Ejercicio 2

EL CONJUNTO RESIDENCIAL CONUCOS DESEA CONSTRUIR UN ALGORITMO QUE LE PERMITA
CONOCER EL TOTAL RECAUDADO POR CONCEPTO DEL PAGO DE LA ADMINISTRACION DE LOS
RESIDENTES. EL CONJUNTO RESIDENCIAL CUENTA CON UN TOTAL DE 20 RESIDENTES. EL
ALGORITMO DEBE PERMITIR REGISTRAR EL VALOR PAGADO POR CADA RESIDENTE. EL VALOR
DE FIJADO POR LA ADMINISTRACION ES DE 200000. EL ALGORITMO DEBE PERMITIR MOSTRAR
LA SIGUIENTE INFORMACION:
1. TOTAL DE DINERO RECAUDADO
2. TOTAL DE DINERO PENDIENTE POR PAGO
3. TOTAL DE RESIDENTES QUE PAGARON EL TOTAL DE LA ADMINISTRACIóN
4. TOTAL DE RESIDENTES QUE NO PAGARON LA ADMINISTRACION
5. TOTAL DE RESIDENTES QUE ABONARON DE LA ADMON

"""

ValorAdmon = 200000
NumRes = 20

TotalRecaudo = 0
TotalPendiente = 0
PagaronTotal = 0
NoPagaron = 0
Abonaron = 0

for i in range(1, NumRes +1):
    pago = float(input(f"ingrese el valor pagado por el residente {i}: "))
    TotalRecaudo += pago
    
    if pago == 0:
        NoPagaron += 1
        TotalPendiente += ValorAdmon
    elif pago == ValorAdmon:
        PagaronTotal += 1
    elif 0 < pago < ValorAdmon:
        Abonaron += 1
        TotalPendiente += (ValorAdmon - pago)
        
print("\n---Resultados---")
print(f"Total de dinero recaudado: ${TotalRecaudo}")
print(f"Total de dinero pendiente por pago: ${TotalPendiente}")
print(f"Total de residentes que pagaron el total de la administración: {PagaronTotal}")
print(f"Total de residentes que NO PAGARON la administración: {NoPagaron}")
print(f"Total de residentes que abonaron a la administración: {Abonaron}")
