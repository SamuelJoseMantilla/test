"""
Nombre: David Andrés Gómez Castro
Fecha: 1 de agosto 2025
Descripciòn: Ejercicio 1


DISEÑAR UN ALGORITMO QUE PERMITA CALCULAR EL SALARIO A PAGAR A UN EMPLEADO. EL
SALARIO BASE DE LOS EMPLEADOS DEPENDERA DE LA CATEGORIA.

LOS EMPRESADOS DE
CATEGORIA A GANAN 2000000, LOS EMPLEADOS DE CATEGORIA B GANAN 2500000 LOS
EMPLEADO DE CATEGORIA C GANAN 3000000.

EL DEPARTAMENTO DE NOMINA REALIZA EL
PROCESO DE LIQUIDACIÓN TENIENDO EN CUENTA LOS SIGUIENTES PARAMETROS:
1. LOS DIAS TRABAJADOS DEL EMPLEADO
2. LAS HRAS EXTRAS TRABAJADAS POR EL EMPLEADO. CADA HRA EXTRA SE PAGA TENIENDO EN
CUENTA SI ES DIURNA O NOCTURNA. LA HRA DIURNA EQUIVALE A 10000 LA HRA NOCTURNA
25000.
3. EL ALGORITMO DEBE MOSTRAR EL SALARIO BASE, EL TOTAL A PAGAR POR CONCEPTO DE
HRAS EXTRAS Y EL SUELDO TOTAL A PAGAR
Grupo: J1
"""


hDiurna = 10000
hNocturna = 25000
A = 2000000
B = 2500000
C = 3000000


print("Categorias disponibles: ")
print("Categoria A: 2000000")
print("Categoria B: 2500000")
print("Categoria A: 3000000")

Cat = str(input("Digite el nivel de categoria A/B/C: ")).upper()
htradia = int(input("Digite el numero de horas extras trabajadas en el día: "))
htranoc = int(input("Digite el numero de horas extras trabajadas en la noche: "))

if Cat == "A":
    print("El salario base es de: ", (A))
    print("Pago de horas extras: ", (htradia*hDiurna) + (htranoc*hNocturna))
    print("El sueldo total a pagar es: ", (A) + (htradia*hDiurna) + (htranoc*hNocturna))
    

elif Cat == "B":
    print("El salario base es de: ", (B))
    print("Pago de horas extras: ", (htradia*hDiurna) + (htranoc*hNocturna))
    print("El sueldo total a pagar es: ", (B) + (htradia*hDiurna) + (htranoc*hNocturna))

elif Cat == "C":
    print("El salario base es de: ", (C))
    print("Pago de horas extras: ", (htradia*hDiurna) + (htranoc*hNocturna))
    print("El sueldo total a pagar es: ", (C) + (htradia*hDiurna) + (htranoc*hNocturna))

else:
    print("Opción no valida")


    
    
    



