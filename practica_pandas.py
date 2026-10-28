"""
================================================================================
INSTITUTO TECNOLÓGICO DE CIUDAD MADERO
Departamento de Sistemas y Computación - Ingeniería en Sistemas Computacionales
Asignatura: Tópicos Avanzados de Programación
Docente: Alejandro Estrada Padilla
Práctica de Laboratorio: Análisis y visualización de calificaciones con Pandas y Matplotlib
Archivo de entrega: practica_pandas.py
================================================================================
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Determinar la ruta base del directorio donde reside este script
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    BASE_DIR = os.getcwd()

# Ruta al archivo calificaciones_isc.csv
csv_path = os.path.join(BASE_DIR, 'calificaciones_isc.csv')
if not os.path.exists(csv_path):
    csv_path = 'calificaciones_isc.csv'

# ==============================================================================
# EJERCICIO 1: CARGA Y REVISIÓN
# ==============================================================================
# ¿Por qué el archivo tiene 288 registros y no 24?
# EXPLICACIÓN / COMENTARIO:
# El conjunto de datos abarca a 24 alumnos en total. Cada uno de los alumnos cursa
# 4 materias diferentes (Programacion, Bases de datos, Redes y Matematicas discretas),
# y cada una de esas materias se evalúa a lo largo de 3 unidades.
# Por lo tanto, el total de registros en la tabla es:
# 24 alumnos × 4 materias × 3 unidades = 288 filas en el DataFrame.

print("=" * 80)
print("EJERCICIO 1: CARGA Y REVISIÓN DE DATOS")
print("=" * 80)

# Cargar el archivo CSV en un DataFrame llamado 'df'
df = pd.read_csv(csv_path)

# 1. Primeras 5 filas
print("\n--- 1. Primeras 5 filas del DataFrame (head) ---")
print(df.head())

# 2. Número de filas y de columnas
filas, columnas = df.shape
print(f"\n--- 2. Dimensiones del DataFrame ---")
print(f"Filas: {filas}, Columnas: {columnas} (shape: {df.shape})")

# 3. Tipo de dato de cada columna
print("\n--- 3. Tipo de dato de cada columna (dtypes) ---")
print(df.dtypes)

# 4. Resumen estadístico de 'calificacion' y de 'asistencias'
print("\n--- 4. Resumen estadístico de calificacion y asistencias (describe) ---")
print(df[['calificacion', 'asistencias']].describe())


# ==============================================================================
# EJERCICIO 2: FILTROS
# ==============================================================================
print("\n" + "=" * 80)
print("EJERCICIO 2: FILTRADO DE DATOS (SIN MODIFICAR df)")
print("=" * 80)

# Filtro 1: Solo alumnos del grupo A
filtro_grupo_a = df[df['grupo'] == 'A']
total_grupo_a = len(filtro_grupo_a)
print(f"\n1. Registros que pertenecen únicamente al Grupo A: {total_grupo_a} filas")

# Filtro 2: Unidades con calificación menor a 70 (reprobadas)
filtro_menor_70 = df[df['calificacion'] < 70]
total_menor_70 = len(filtro_menor_70)
print(f"2. Registros con calificación menor a 70 (< 70): {total_menor_70} filas")

# Filtro 3: Materia 'Bases de datos', del grupo B, con calificación de al menos 80 (>= 80)
filtro_bd_b_80 = df[(df['materia'] == 'Bases de datos') & (df['grupo'] == 'B') & (df['calificacion'] >= 80)]
total_bd_b_80 = len(filtro_bd_b_80)
print(f"3. Registros de 'Bases de datos' en Grupo B con calificación >= 80: {total_bd_b_80} filas")


# ==============================================================================
# EJERCICIO 3: COLUMNA CALCULADA
# ==============================================================================
print("\n" + "=" * 80)
print("EJERCICIO 3: COLUMNA CALCULADA ('situacion')")
print("=" * 80)

# Crear la columna 'situacion' usando np.where (vectorizado, sin ciclos for)
# Condición: si calificacion >= 70 es 'Aprobado', de lo contrario 'Reprobado'
df['situacion'] = np.where(df['calificacion'] >= 70, 'Aprobado', 'Reprobado')

print("\nMuestra de las primeras 10 filas con la nueva columna 'situacion':")
print(df[['matricula', 'nombre', 'materia', 'unidad', 'calificacion', 'situacion']].head(10))


# ==============================================================================
# EJERCICIO 4: RESÚMENES ESTADÍSTICOS Y EXPORTACIÓN
# ==============================================================================
print("\n" + "=" * 80)
print("EJERCICIO 4: RESÚMENES CON GROUPBY Y EXPORTACIÓN CSV")
print("=" * 80)

# 1. Promedio de calificación por materia
promedio_materia = df.groupby('materia')['calificacion'].mean()
print("\n--- 1. Promedio de calificación por materia ---")
print(promedio_materia.round(2))

# 2. Promedio por grupo y materia
promedio_grupo_materia = df.groupby(['grupo', 'materia'])['calificacion'].mean()
print("\n--- 2. Promedio por grupo y materia ---")
print(promedio_grupo_materia.round(2))

# 3. Promedio general de cada alumno, ordenado de mayor a menor
promedios_alumnos = df.groupby(['matricula', 'nombre'])['calificacion'].mean().reset_index()
promedios_alumnos = promedios_alumnos.rename(columns={'calificacion': 'promedio'})
promedios_alumnos = promedios_alumnos.sort_values(by='promedio', ascending=False)
print("\n--- 3. Promedio general de cada alumno (ordenado de mayor a menor) ---")
print(promedios_alumnos.to_string(index=False))

# 4. Promedio general por unidad, con todas las materias juntas
promedio_unidad = df.groupby('unidad')['calificacion'].mean()
print("\n--- 4. Promedio general por unidad ---")
print(promedio_unidad.round(2))

# 5. Cuántas unidades salieron aprobadas y cuántas reprobadas
conteo_situacion = df['situacion'].value_counts()
print("\n--- 5. Conteo de unidades aprobadas y reprobadas ---")
print(conteo_situacion)

# Exportar el promedio por alumno a promedios_alumnos.csv sin guardar el índice
promedios_alumnos.to_csv(os.path.join(BASE_DIR, 'promedios_alumnos.csv'), index=False)
print("\n--> Archivo 'promedios_alumnos.csv' exportado exitosamente sin la columna de índice.")


# ==============================================================================
# EJERCICIO 5: GRÁFICAS CON MATPLOTLIB
# ==============================================================================
print("\n" + "=" * 80)
print("EJERCICIO 5: GENERACIÓN DE GRÁFICAS")
print("=" * 80)

# NOTA DE BUENAS PRÁCTICAS:
# Según las indicaciones de la práctica y para evitar imágenes vacías,
# siempre se llama a savefig() ANTES de plt.show() (o plt.close()).

# ------------------------------------------------------------------------------
# Figura 1: Barras del promedio por materia (Eje Y de 0 a 100)
# ------------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
colores_barras = ['#3498db', '#2ecc71', '#e67e22', '#9b59b6']
barras = plt.bar(promedio_materia.index, promedio_materia.values, color=colores_barras, edgecolor='black', width=0.55)

plt.title('Promedio de Calificación por Materia', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Materia', fontsize=12, fontweight='bold')
plt.ylabel('Calificación Promedio', fontsize=12, fontweight='bold')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar etiquetas con los valores exactos sobre cada barra
for b in barras:
    altura = b.get_height()
    plt.text(b.get_x() + b.get_width() / 2.0, altura + 1.5, f"{altura:.2f}",
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'promedio_materias.png'), dpi=300)
print("--> Gráfica 1 guardada como: promedio_materias.png")
plt.close()

# ------------------------------------------------------------------------------
# Figura 2: Histograma de todas las calificaciones con línea vertical en 70
# ------------------------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df['calificacion'], bins=12, color='#5dade2', edgecolor='black', alpha=0.8)
plt.axvline(x=70, color='red', linestyle='--', linewidth=2.5, label='Calificación Aprobatoria (70)')

plt.title('Distribución General de Calificaciones', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Calificación Obtenida', fontsize=12, fontweight='bold')
plt.ylabel('Frecuencia (Cantidad de Unidades Evaluadas)', fontsize=12, fontweight='bold')
plt.legend(loc='upper left', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'histograma.png'), dpi=300)
print("--> Gráfica 2 guardada como: histograma.png")
plt.close()

# ------------------------------------------------------------------------------
# Figura 3: Líneas del promedio por unidad, una línea por materia
# ------------------------------------------------------------------------------
# Agrupamos por unidad y materia para obtener la matriz pivote
tendencia = df.groupby(['unidad', 'materia'])['calificacion'].mean().unstack()

plt.figure(figsize=(9, 5.5))
marcadores = ['o', 's', '^', 'D']
for idx, materia in enumerate(tendencia.columns):
    plt.plot(tendencia.index, tendencia[materia],
             marker=marcadores[idx % len(marcadores)],
             linewidth=2.2, markersize=8, label=materia)

plt.title('Tendencia del Promedio por Unidad según la Materia', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Unidad de Evaluación', fontsize=12, fontweight='bold')
plt.ylabel('Calificación Promedio', fontsize=12, fontweight='bold')
plt.xticks([1, 2, 3], ['Unidad 1', 'Unidad 2', 'Unidad 3'], fontsize=11)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Materias', fontsize=10, loc='best')

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, 'tendencia_unidades.png'), dpi=300)
print("--> Gráfica 3 guardada como: tendencia_unidades.png")
plt.close()


# ==============================================================================
# EJERCICIO 6: LECTURA DE RESULTADOS E INTERPRETACIÓN
# ==============================================================================
# Con base en los resúmenes calculados y las gráficas generadas:
#
# 1. ¿Qué materia quedó con el promedio más bajo?
#    Respuesta: La materia con el promedio más bajo es "Matematicas discretas",
#    con una calificación promedio general de 66.08 (siendo la única materia
#    con promedio grupal por debajo de los 70 puntos reglamentarios).
#
# 2. ¿Si el promedio general de la unidad 3 es menor que el de las unidades 1 y 2?
#    Respuesta: Sí. El promedio general de la Unidad 3 es de 69.79 puntos,
#    el cual es efectivamente menor que el promedio de la Unidad 1 (73.75)
#    y el de la Unidad 2 (73.16), evidenciando un descenso en el rendimiento hacia
#    el cierre del semestre.
#
# 3. ¿Cuántos alumnos quedan bajo 70 en su promedio general?
#    Respuesta: Un total de 7 alumnos obtuvieron un promedio general por debajo
#    de 70 puntos (reprobados en el promedio final acumulado).
# ==============================================================================

print("\n" + "=" * 80)
print("EJERCICIO 6: INTERPRETACIÓN DE RESULTADOS")
print("=" * 80)
materia_min = promedio_materia.idxmin()
val_min = promedio_materia.min()
print(f"1. Materia con promedio más bajo: {materia_min} ({val_min:.2f})")
print(f"2. Promedios por unidad -> Unidad 1: {promedio_unidad[1]:.2f}, Unidad 2: {promedio_unidad[2]:.2f}, Unidad 3: {promedio_unidad[3]:.2f}")
es_menor = promedio_unidad[3] < promedio_unidad[1] and promedio_unidad[3] < promedio_unidad[2]
print(f"   ¿La unidad 3 es menor que la 1 y 2? {'Sí' if es_menor else 'No'}")
alumnos_bajo_70 = len(promedios_alumnos[promedios_alumnos['promedio'] < 70])
print(f"3. Alumnos con promedio general menor a 70: {alumnos_bajo_70} alumnos de {len(promedios_alumnos)}")
print("=" * 80)
print("¡Práctica completada con éxito!")
