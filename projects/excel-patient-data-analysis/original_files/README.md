# Proyecto Excel: Limpieza y Análisis de Datos de Pacientes

Este proyecto presenta una actividad práctica de Excel enfocada en **limpieza de datos, documentación de errores, corrección de registros, análisis descriptivo y comunicación de insights**.

El objetivo fue trabajar con archivos de datos de pacientes en Excel para revisar la calidad del dataset, detectar anomalías, aplicar correcciones, crear estadísticas básicas, construir tablas resumen y preparar una explicación clara para una presentación corta.

> Nota: este proyecto se presenta con fines académicos y de portafolio. Si los datos fueran reales, no deberían publicarse con nombres, fechas de nacimiento u otra información identificable.

## Enlace de presentación en Canva

https://canva.link/4t7szd1apthwldm

## Archivos incluidos

```text
projects/excel-patient-data-analysis/
├── README.md
└── original_files/
    ├── Actividad_Analisis_Datos_Pacientes_corregido.xlsx
    └── Datos_Ejemplo_Corregido.xlsx
```

## Descripción de los archivos

### 1. Datos_Ejemplo_Corregido.xlsx

Este archivo corresponde a la parte de **limpieza y corrección de datos**.

Incluye hojas para:

- Dataset original importado desde CSV.
- Registro de errores encontrados.
- Registro de correcciones aplicadas.
- Dataset corregido.

En este archivo se trabajó la identificación de problemas como:

- Valores faltantes en edad, género, diagnóstico y seguro médico.
- Inconsistencias en fechas de ingreso y fecha de alta.
- Días hospitalizados negativos o inconsistentes.
- Problemas de codificación en nombres y diagnósticos con tildes.
- Estandarización de valores vacíos a categorías como `N/A`, `No especificado` o `No registrado`.

### 2. Actividad_Analisis_Datos_Pacientes_corregido.xlsx

Este archivo corresponde a la parte de **análisis descriptivo y presentación de resultados**.

Incluye hojas para:

- Datos principales del análisis.
- Estadísticas básicas.
- Tablas resumen.
- Gráficos.

En este archivo se aplicaron funciones y herramientas de Excel para obtener métricas como conteos, promedios, mínimos, máximos, agrupaciones y visualizaciones.

## Qué hice en el proyecto

1. Revisé inicialmente los archivos para entender columnas, tipos de datos y estructura general.
2. Identifiqué errores y anomalías en las columnas principales.
3. Documenté los errores encontrados en una hoja específica.
4. Apliqué correcciones sobre valores faltantes, fechas inconsistentes y categorías no definidas.
5. Generé una versión corregida del dataset.
6. Calculé estadísticas básicas con funciones de Excel.
7. Creé tablas resumen por variables relevantes como género, seguro médico y diagnóstico.
8. Elaboré gráficos para visualizar patrones importantes.
9. Redacté conclusiones para explicar los resultados en una presentación corta.

## Insights principales

A partir de la revisión de los datos se observaron los siguientes hallazgos:

- El dataset contiene aproximadamente **5,000 registros de pacientes**.
- No se identificaron IDs de paciente duplicados.
- Se encontraron valores faltantes en campos importantes como edad, género, diagnóstico y seguro médico.
- Una parte importante de los registros no tenía seguro médico informado o aparecía como `N/A`.
- Se detectaron inconsistencias fuertes en fechas, especialmente casos donde la fecha de alta no coincidía con la fecha de ingreso más los días hospitalizados.
- También aparecieron registros donde la fecha de alta era anterior a la fecha de ingreso, lo cual es un error lógico.
- La edad promedio observada en el archivo de análisis fue de aproximadamente **46 años**.
- El promedio de días hospitalizados fue de aproximadamente **19 días**.
- Los diagnósticos con mayor presencia incluyeron diabetes, hipertensión, neumonía y COVID-19.
- El análisis permitió transformar una tabla inicial con errores en un archivo más claro, documentado y útil para tomar decisiones.

## Interpretación del análisis

El proyecto muestra la importancia de revisar la calidad de los datos antes de analizarlos. Aunque el dataset permitía calcular estadísticas y crear gráficos, existían errores que podían afectar las conclusiones, especialmente en fechas, categorías vacías y campos clínicos incompletos.

Después de documentar y corregir las anomalías, el archivo quedó mejor preparado para análisis descriptivo. Las tablas resumen y gráficos permiten identificar patrones generales en los pacientes, como distribución por género, tipo de seguro, diagnóstico y comportamiento de hospitalización.

Este ejercicio demuestra habilidades básicas pero importantes para un perfil de **Data Analyst / BI inicial**, especialmente en:

- Limpieza de datos en Excel.
- Documentación de errores.
- Validación de calidad de datos.
- Análisis descriptivo.
- Creación de tablas resumen.
- Visualización de información.
- Comunicación de resultados.

## Herramientas utilizadas

- Microsoft Excel
- Funciones básicas de Excel: conteo, promedio, mínimo y máximo
- Tablas resumen
- Gráficos
- Canva para la presentación

## Próximas mejoras posibles

- Crear una versión anonimizada para publicación pública.
- Agregar un dashboard más visual en Excel o Power BI.
- Repetir el análisis usando Python con pandas.
- Documentar el proceso paso a paso con capturas.
- Crear una presentación final de 2 a 4 minutos explicando hallazgos y decisiones de limpieza.
