# Análisis y Visualización de Calificaciones con Pandas y Matplotlib

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557c.svg)](https://matplotlib.org/)

Proyecto de laboratorio para el análisis exploratorio y visualización de datos de calificaciones de estudiantes de Ingeniería en Sistemas Computacionales (ISC), desarrollado con las librerías **Pandas** y **Matplotlib**.

---

## 🏛️ Contexto Académico
- **Institución:** Instituto Tecnológico de Ciudad Madero (ITCM)
- **Departamento:** Sistemas y Computación
- **Carrera:** Ingeniería en Sistemas Computacionales
- **Asignatura:** Tópicos Avanzados de Programación
- **Docente:** Alejandro Estrada Padilla

---

## 📁 Estructura del Proyecto

```text
├── calificaciones_isc.csv     # Dataset base (288 registros: 24 alumnos × 4 materias × 3 unidades)
├── practica_pandas.py         # Script principal de ejecución en Python
├── practica_pandas.ipynb      # Cuaderno interactivo Jupyter Notebook con desarrollo guiado
├── promedios_alumnos.csv      # Exportación de promedios ordenados por alumno
├── promedio_materias.png      # Gráfica 1: Calificación promedio por materia
├── histograma.png             # Gráfica 2: Histograma de distribución de calificaciones
├── tendencia_unidades.png     # Gráfica 3: Tendencia de calificaciones a través de las unidades
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

---

## 📊 Descripción del Conjunto de Datos (`calificaciones_isc.csv`)

El archivo CSV contiene **288 filas** y **7 columnas**:
- `matricula`: Clave única del alumno (ej. `ISC240100`).
- `nombre`: Nombre completo del estudiante.
- `grupo`: Grupo asignado (`A` o `B`).
- `materia`: Asignatura (`Programacion`, `Bases de datos`, `Redes`, `Matematicas discretas`).
- `unidad`: Unidad evaluada (`1`, `2` o `3`).
- `calificacion`: Calificación obtenida (escala 0 a 100).
- `asistencias`: Sesiones asistidas durante la unidad.

> **¿Por qué son 288 registros y no 24?**  
> Porque hay 24 alumnos registrados, cada uno cursando 4 materias distintas, y cada materia se evalúa a lo largo de 3 unidades:  
> **24 alumnos × 4 materias × 3 unidades = 288 registros**.

---

## 🛠️ Ejercicios Implementados

### 1. Carga y Revisión
- Carga eficiente de datos en DataFrame con `pd.read_csv()`.
- Inspección inicial (`head()`, `shape`, `dtypes`).
- Análisis estadístico descriptivo (`describe()`) de calificaciones y asistencias.

### 2. Filtrado Booleano de Datos
- Filtrado de registros exclusivos del **Grupo A** (144 registros).
- Filtrado de unidades reprobadas con calificación **< 70** (120 registros).
- Filtrado específico para **Bases de datos** en **Grupo B** con calificación **≥ 80** (16 registros).

### 3. Columna Calculada
- Incorporación vectorizada de la columna `situacion` mediante `np.where`:
  $$\text{situacion} = \begin{cases} \text{'Aprobado'} & \text{si calificacion} \ge 70 \\ \text{'Reprobado'} & \text{si calificacion} < 70 \end{cases}$$
- Resultado: 168 unidades aprobadas y 120 reprobadas.

### 4. Resúmenes Estadísticos y Exportación
- Promedios por materia y desglose por grupo con `groupby()`.
- Cálculo del promedio general por alumno ordenado de mayor a menor.
- Exportación del reporte ordenado a `promedios_alumnos.csv` sin columna de índice.

### 5. Generación de Gráficas con Matplotlib
1. **`promedio_materias.png`**: Diagrama de barras con etiquetas de valor en cada columna y rango de 0 a 100 en el eje Y.
2. **`histograma.png`**: Distribución general de calificaciones con línea roja discontinua señalando el umbral de aprobación en 70.
3. **`tendencia_unidades.png`**: Gráfica de líneas multigrupo mostrando la evolución del rendimiento por materia de la Unidad 1 a la 3.

### 6. Hallazgos e Interpretación de Resultados
1. **Materia con menor promedio:** *Matemáticas discretas* (66.08), siendo la única materia con promedio grupal reprobatorio.
2. **Comportamiento por unidad:** El promedio general desciende progresivamente hacia el cierre del semestre:
   - Unidad 1: **73.75**
   - Unidad 2: **73.16**
   - Unidad 3: **69.79** (menor que las unidades previas).
3. **Alumnos con promedio reprobatorio:** **7 de los 24 alumnos** obtuvieron un promedio general inferior a 70 puntos.

---

## 🚀 Instalación y Ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/victorzavala0ei-lang/practica-pandas-matplotlib.git
   cd practica-pandas-matplotlib
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar el script:
   ```bash
   python practica_pandas.py
   ```

4. Para explorar interactivamente el Jupyter Notebook:
   ```bash
   jupyter notebook practica_pandas.ipynb
   ```
