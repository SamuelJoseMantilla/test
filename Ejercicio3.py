"""
    Autor: David Andrés Gómez Castro
    Fecha: 04 agosto 2025
    Descripción: Ejercicio 3
    
    EL PROFESOR DE MATEMATICAS DESEA CONSTRUIR UN ALGORITMO QUE LE PERMITA CALCULAR
LA NOTA FINAL DE LOS ESTUDIANTES DE SUGRUPO DE MATEMATICAS DISCRETAS. TENGA EN
CUENTA LOS SIGUIENTES REQUERIMIENTOS:
1. EL GRUPO ESTA CONDORMADO POR 10 ESTUDIANTES
2. LA NOTAS ESTA DIVIDIDAS EN PARCIALES, QUICES Y TRABAJOS. LOS PARCIALES TIENEN UN
VALOR DEL 60% DE LA ASIGNATURA, LOS QUICES TIENEN UN VALOR DEL 25% Y LOS
TRABAJOS UN VALOR DEL 15%.
3. EL PROGRAMA DEBE MOSTRAR EL SIGUIENTE RESUMEN ACADEMICO:
A. PROMEDIO GENERAL DEL GRUPO
B. TOTAL DE ESTUDIANTES QUE APROBARON LA ASIGNATURA
C. TOTAL DE ESTUDIANTES QUE REPOBARON LA ASIGNATURA.
D. TOTAL DE ESTUDIANTES QUE OBTUVIERON UNA NOTA ENTRE 1 Y 2.9
E. TOTAL DE ESTUDIANTES QUE OBTUVIERON UNA NOTA ENTRE 3.0 Y 3.5F. NOTA MAS ALTA DEL GRUPO
G. NOTA MAS BAJA DEL GRUPO
H. TOTAL DE ESTUDIANTES QUE OBTUVIERON UNA NOTA SUPERIOR AL PROMEDIO
GENERAL.
    
"""

NumEst = 10

def calcular_nota_final(parciales, quices, trabajos):
    return parciales * 0.6 + quices * 0.25 + trabajos * 0.15

notas_finales = []

print("Ingrese las notas de los estudiantes (valores entre 0 y 5):\n")

for i in range(NumEst):
    print(f"Estudiante #{i+1}")
    while True:
        try:
            parciales = float(input("  Nota de parciales: "))
            quices = float(input("  Nota de quices: "))
            trabajos = float(input("  Nota de trabajos: "))
            if all(0 <= n <= 5 for n in [parciales, quices, trabajos]):
                break
            else:
                print("  Las notas deben estar entre 0 y 5. Intente de nuevo.")
        except ValueError:
            print("  Entrada inválida. Intente de nuevo.")
    
    nota_final = calcular_nota_final(parciales, quices, trabajos)
    notas_finales.append(nota_final)


promedio_general = sum(notas_finales) / NumEst
aprobados = sum(1 for nota in notas_finales if nota >= 3.0)
reprobados = NumEst - aprobados
entre_1_y_2_9 = sum(1 for nota in notas_finales if 1.0 <= nota <= 2.9)
entre_3_y_3_5 = sum(1 for nota in notas_finales if 3.0 <= nota <= 3.5)
nota_mas_alta = max(notas_finales)
nota_mas_baja = min(notas_finales)
superiores_al_promedio = sum(1 for nota in notas_finales if nota > promedio_general)


print("\n--- RESUMEN ACADÉMICO ---")
print(f"Promedio general del grupo: {promedio_general:.2f}")
print(f"Total de estudiantes que aprobaron la asignatura: {aprobados}")
print(f"Total de estudiantes que reprobaron la asignatura: {reprobados}")
print(f"Estudiantes con nota entre 1.0 y 2.9: {entre_1_y_2_9}")
print(f"Estudiantes con nota entre 3.0 y 3.5: {entre_3_y_3_5}")
print(f"Nota más alta del grupo: {nota_mas_alta:.2f}")
print(f"Nota más baja del grupo: {nota_mas_baja:.2f}")
print(f"Estudiantes con nota superior al promedio general: {superiores_al_promedio}")
