# PI_DA
HENRY - PROYECTO INDIVIDUAL Nº2 - Data Analyst - Siniestros viales en CABA

<a href="https://www.python.org/">![Python](https://img.shields.io/badge/Python-3.10.12-3776AB?style=for-the-bage&logo=Python)</a> <a href="https://numpy.org/">![NumPy](https://img.shields.io/badge/NumPy-1.25.2-013243?style=for-the-bage&logo=numpy)</a> <a href="https://jupyter.org/">![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-1.0.0-F37626?style=for-the-bage&logo=jupyter)</a> <a href="https://pandas.pydata.org/">![Pandas](https://img.shields.io/badge/Pandas-2.1.0-150458?style=for-the-bage&logo=pandas)</a> <a href="https://matplotlib.org">![matplotlib](https://img.shields.io/badge/matplotlib-3.5.1-4285F4?style=for-the-bage&logo=exordo)</a> <a href="https://seaborn.pydata.org/">![seaborn](https://img.shields.io/badge/seaborn-0.13.0-4285F4?style=for-the-bage&logo=flood)</a> <a href="https://code.visualstudio.com/">![VSC](https://img.shields.io/badge/Visual_Studio_Code-1.85-007ACC?style=for-the-bage&logo=visualstudiocode)</a>

![Texto alternativo](src/portada.png?id=27084445&width=1245&height=700&quality=85&coordinates=0%2C0%2C0%2C0)

### Descripción del Problema
Los siniestros viales, eventos que involucran vehículos en las vías públicas, son una preocupación importante en ciudades como Buenos Aires debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden tener consecuencias graves, incluyendo daños materiales, lesiones y muertes.

Las tasas de mortalidad por siniestros viales son un indicador clave de la seguridad vial. Reducir estas tasas es un objetivo crucial para proteger la vida de las personas.

La prevención de siniestros viales requiere medidas como educación vial, cumplimiento de normas de tráfico, infraestructura segura y promoción de vehículos más seguros. El seguimiento de estadísticas y la implementación de políticas efectivas son esenciales para abordar este problema.

La alta densidad de tráfico y población en Buenos Aires aumenta la gravedad de los siniestros viales. La urgencia de abordar este problema se refleja en las cifras.

En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales, siendo la principal causa de muertes violentas. Entre 2018 y 2022 se registraron 19.630 muertes en todo el país, equivalentes a 11 personas por día.

En 2022, se contabilizaron 3.828 muertes fatales. La probabilidad de morir en un siniestro vial en Argentina es dos o tres veces mayor que en un hecho de inseguridad delictiva.

### La Tarea
El Observatorio de Movilidad y Seguridad Vial de Buenos Aires (OMSV) nos pide un análisis y visualización de datos sobre seguridad vial en Buenos Aires con el objetivo es obtener información valiosa para tomar medidas y reducir las víctimas fatales en siniestros viales. Para ello se pide analizar datos de homicidios en siniestros viales entre 2016 y 2021 para que las autoridades puedan tomar medidas y reducir las víctimas fatales. Nos dan un dataset en formato xlsx con dos hojas: hechos y víctimas, y dos hojas adicionales con diccionarios de datos para entender mejor la información.

#### Se realizarán:

- Análisis exploratorio de datos: para comprender mejor la información y detectar patrones.
- Diseño y desarrollo de un Dashboard interactivo: con filtros para explorar detalladamente los datos.
- Visualización clara y atractiva de la información: mediante gráficos y otras herramientas visuales.

#### Esperando que el proyecto ayude a la ciudad a:

- Identificar los principales factores que contribuyen a los siniestros viales.
- Desarrollar estrategias y políticas públicas más efectivas para mejorar la seguridad vial.
- Salvar vidas y reducir el número de víctimas fatales.

### Fuente de los datos
Contamos con uns archivos en formato excel (xlsx) y contiene dos hojas llamadas: hechos y víctimas. Asimismo incluye otras dos hojas adicionales de diccionarios de datos.

### Estructura de directorios

A continuación, se presenta la estructura de directorios del proyecto:

<span style="color:#f6a700;">__PI_DA__</span><br>
├── <span style="color:#f6a700;">__src__</span>: Ubicación de los archivos fuente en un proyecto.<br>
|&emsp; ├── <span style="color:#f6a700;">__dashboard__</span>:  Se encuentra almacenado el dashboard SiniestrosViales de extensión .pbix (desarrollado en Power Bi).<br>
│&emsp; │&emsp; └── <span style="color:#f6a700;">__PI2_03.pbix__</span>: <br>
│&emsp; │<br>
│&emsp; ├── <span style="color:#f6a700;">__datasource__</span>: Almacena los datasets fuentes y los resultantes despues del ETL y EDA, en una versión limpia y procesada.<br>
│&emsp; │&emsp; ├── <span style="color:#f6a700;">__dfHechos.csv__</span> <br>
│&emsp; │&emsp; ├── <span style="color:#f6a700;">__dfHechosVictimas.csv__</span> <br>
│&emsp; │&emsp; └── <span style="color:#f6a700;">__homicidios.xlsx__</span> <br>
│&emsp; │<br>
│&emsp; └── <span style="color:#f6a700;">__notebooks__</span>: Contiene los notebooks (.ipynb) con el código completo y bien comentado tanto del ETL como del EDA.<br>
│<br>
└──  <span style="color:#f6a700;">__README.md__</span>: Este es el archivo de descripción del proyecto.<br>




### Limpieza de datos.
El enfoque utilizado fue el tomar los datos de la fuente sin pensar, en un principio en el problema planteado y dedicarnos solo a buscar datos nulos, datos atípicos, tipos de datos, errores de sintaxis. Luego de esta primera pasada por los datos, sí se empezaron a mirar teniendo en cuenta el problema planteado y proporcionar a la etapa de EDA la mayor cantidad de datos oportunos para el análisis:
- Quitamos la columna cruce porque la mayoría de sus valores eran nulos.
- Encontramos datos de tipo texto tal como ‘SD’. Luego de verificar en el diccionario de datos supimos que es la manera de indicar que no se tiene el dato (Sin Dato). Para ayudar a las bibliotecas que fueron importadas en este proyecto, la valores ‘SD’ fueron convertidos a nulos (NaN).
- Cuando encontramos pocos valores en alguna columna, tratamos de imputarla entes que eliminarla buscando pistas en el resto del dataset.
- En la columna ‘SEXO’ reemplazamos los valores nulos estimando la proporción actual de dataset buscando siempre mantener el equilibrio del mismo.
- Hubo valores nulos que pudieron ser plausibles ya que el momento del siniestro pudo haber ocurrido que resultara determinar el sexo de la victima.
- Se usó el criterio de mantener el tipo de dato lo más acorde al estándar. Por ejemplo, si el mes enero era representado con un ‘1’ y era una cadena de texto de un dígito, entonces esa cadena quedó convertida a entero de 8 bits logrando así optimizar el uso de espacio en memoria.
- Al ver que los títulos de la mayoría de las columnas estaban en mayúsculas y que cuando dicho título estaba formado por más de un palabra separadas por un guion bajo ‘_’ se decidió que los títulos de todas las columna debían seguir este patrón.
- Para la imputación de los datos se utilizaron técnicas como la media o la mediana. 
- Las variables 'XY_(CABA)', 'POS_X' y 'POS_Y' son columnas de datos geoespaciales lo que implica un tratamiento especial siendo el tipo de dato un poco mas complejo. Los datos geoespaciales no son simplemente números o cadenas de texto, son datos espaciales que representan entidades del mundo real como puntos, lineas y polígonos. Estos datos requieren un tratamiento especial debido a su complejidad y a las diferentes formas en que pueden ser representados y almacenados. Existen diferentes sistemas de coordenadas como el Sistema de Coordenadas Geodesicas Mundial (WGS84) y el Sistema de Coordenadas Universal Transversal de Mercator (UTM). El más común es UTM pero según el diccionario de datos que acompaña al dataset del proyecto, las coordenadas de las columnas 'POS_X' y 'POS_Y' están en WGS84. En cambio, la columna 'XY_(CABA)' utiliza un sistema de referencia bidimensional que se utiliza para definir la ubicación de puntos en un plano. Se define por dos ejes perpendiculares entre si, generalmente llamados eje X y eje Y. En consecuencia hemos decidido sacar estas tres columnas porque no utilizaremos graficas de mapas para la representación geoespacial.
          
### Creación de variables
- Calcular la tasa de homicidios en siniestros viales para cada mes del período de estudio.
- Identificar los accidentes mortales con víctimas en moto.
- Se creó una nueva columna ‘PARTES_DIA’ para explorar las tendencias de los siniestros según el momento del día en que éstos ocurren:

### Análisis descriptivo
1- Distribución de las variables. Las variables fueron divididas y analizadas en dos grandes grupos:
  - Categóricas. Analizamos la distribución de variables categóricas como TIPO_DE_CALLE, SEXO, ROL, etc. mediante tablas de frecuencia.
  - Numéricas. Visualizamos la distribución de variables numéricas como N_VICTIMAS, ALTURA, EDAD, etc. mediante histogramas o diagramas de caja.

2- Medidas de resumen
  - Calculamos medidas como la media, la mediana, la moda y la desviación estándar para las variables numéricas.
  - Calculamos frecuencias absolutas y relativas para las variables categóricas (count()).

3- Análisis de correlaciones
  - Identificamos posibles relaciones entre las variables mediante el uso de bibliotecas de apoyo como matplotlib y seaborne.

### Visualización de datos

Power BI es una plataforma para la inteligencia empresarial (BI) que permite conectar datos, visualizarlos e incrustar objetos visuales muy facilmente. Con Power BI, es posible crear cuadros de mando que faciliten la toma de decisiones, actualizar la información de manera automatizada o manual, y compartir el resultado de manera interactiva.
Usando esta plataforma de Microsoft en su versión gratuita pudimos terminar de ajustar los datos y completar el análisis para su visualización. 

1- Visión general
  - Visualizar la panorámica general de los datos en el contexto de los siniestros ocurridos en la ciudad de Buenos Aires.
  - Visualizar la distribución espacial de los siniestros viales en CABA.
  - Identificar zonas con mayor concentración de accidentes.

2- Hechos ocurridos entre 2016 al 2021
  - Visualizar la evolución de la tasa de homicidios en siniestros viales y la cantidad de accidentes mortales con víctimas en moto a lo largo del tiempo.
  - Evaluar el progreso hacia el cumplimiento de los KPIs.

3- Indicador clave de rendimiento para siniestros semestrales
  - Descripción del objetivo de alcanzar el 10% de reducción en la tasa de accidentes en CABA con respecto al semestre anterior.
  - Identificar posibles patrones o relaciones no lineales.

4- Indicador clave de rendimiento para accidentes en monto cada año
  - Descripción del objetivo de alcanzar el 7% de reducción en la cantidad de accidentes mortales en moto respecto al año anterior el la ciudad de Buenos Aires.
  - Tuvimos en cuenta los accidentes en moto según la franja horaria en el transcurso del día. Las partes del día se clasificaron en mañana, mediodía, tarde, noche, medianoche y madrugada:
            ▪ - Medianoche que corresponde a la hora doce del periodo nocturno. De 0:00 a 1:00
            ▪ - Madrugada que va desde la medianoche hasta que sale el sol. De 1:00 a 6:30
            ▪ - Mañana que corresponde al periodo desde que sale el sol hasta el mediodía. De 6:30 a 12:00
            ▪ - Mediodía que corresponde a la hora doce del periodo diurno. De 12:00 a 13:00
            ▪ - Tarde que corresponde al periodo desde el mediodía hasta que se pone el sol. De 13:00 a 20:00
            ▪ - Noche que corresponde desde que se pone el sol hasta la medianoche. De 20:00 a 0:00

### Interpretación y generación de insights
1- Observaciones
  - Se desconocen a los acusados en 21 hechos.
  - La tendencia del quinquenio es un descenso en la siniestralidad de 141 en el 2016 a 97 en el 2021.
  - Hay una clara caída en la siniestralidad entre el segundo semestre del 2018 y el primer semestre del 2020.
  - El segundo semestre del 2016 es el periodo de tiempo con más siniestros en el quinquenio.
  - El primer semestre del 2020 es el punto mas bajo de la siniestralidad del quinquenio.
  - Presentar los hallazgos de manera clara y concisa a las partes interesadas.
  - Diciembre tiende a ser el mes con mayor numero de siniestros.
  - Agosto tiende a ser el mes de menor siniestralidad.
  - Los primeros tres meses del año tiende a bajar el numero de casos mientras que en los últimos tres meses tiende a subir.
  - El día ocho de cada mes es el que presenta menor numero de casos. No tomamos en cuenta el 31 de cada mes porque al año solo hay siete.
  - Los días 17 y 20 de cada mes son los que presentan mayor numero de casos.
  - Hay una clara tendencia a disminuir la siniestralidad en la ultima semana de cada mes.
  - Los autos y los pasajeros de unidades de transporte público son los que causan la mayoría de accidentes.
  - Los trenes intervienen muy poco en los siniestros.
  - La mayoría de los hechos ocurren en la comuna 1.
  - La mayoría de los hechos ocurren en las avenidas.
  - El cruce mas peligroso es PAZ, GRAL AV.
  - La mayoría de los hechos le ocurren a personas de entre 20 y 40 años.
  - Son mucho más hombres que mujeres involucrados en los siniestros.
  - La mayoría de las victimas en moto tenían entre 20 y 40 años de edad.
  - En el rango del adulto mayor (60~100 años)resulta ser la victima mas frecuente de siniestros.
  - En la mayoría de los años hubo mas frecuencia de siniestros en el segundo semestre del año.
  - Del 2019 al 2021 se nota un descenso general en el numero de siniestros.
  - La reducción de la tasa de accidentes fatales respecto al semestre anterior se logra en los años 2019 y 2021. 
  - El porcentaje de accidentes fatales en moto se reduce en más del 7% en los años 2017 y 2020.


### Consideraciones adicionales

1- Enfocarse en los tipos de víctimas más vulnerables:
  - Motociclistas: Implementar campañas de concienciación a jóvenes motociclistas sobre la seguridad vial para este grupo, incluyendo el uso obligatorio de cascos y equipamiento adecuado.
  - Peatones: Mejorar la infraestructura vial para la seguridad de peatones pensando en el adulto mayor, como la construcción de aceras, pasos de peatones y ciclovías.

2- Reducir la velocidad en zonas de alto riesgo:
  - Implementar en vías de alto riesgo como las avenidas General Paz, Escalada, Rivadavia e Independencia medidas de control de velocidad como reductores de velocidad, radares y mayor presencia policial.

3- Mejorar la atención médica en caso de accidentes:
  - Implementar programas de formación para el personal de primeros auxilios y atención médica en casos de accidentes de tráfico.
  - Asegurar la disponibilidad de recursos médicos y ambulancias en zonas con alta incidencia de accidentes.

4- Fortalecer las medidas de control y sanción:
  - Aplicar multas y sanciones más severas para conductores que infrinjan las normas de tránsito, como conducir bajo la influencia del alcohol o exceso de velocidad.
  - Implementar programas de reeducación vial para conductores que infrinjan las normas de tránsito.

5- Recopilación y análisis de datos:
  - Implementar un sistema de recopilación de datos más robusto y preciso sobre accidentes de tránsito, incluyendo información sobre las causas, las víctimas y las condiciones ambientales.
  - Utilizar el análisis de datos para identificar patrones y factores de riesgo en los accidentes de tránsito.

6- Campañas de concienciación vial:
  - Implementar campañas de concienciación vial dirigidas a toda la población, en especial a las comunas 1, 4, 9 y 8, incluyendo conductores, motociclistas, peatones y ciclistas.

7- Investigación e innovación:
  - Invertir en investigación para desarrollar nuevas tecnologías y estrategias para la prevención de accidentes de tránsito.
  - Implementar programas de innovación para mejorar la seguridad vial.

8- Cooperación entre diferentes actores:
  - Fomentar la cooperación entre el gobierno, las organizaciones no gubernamentales, las empresas y la sociedad civil para la prevención de accidentes de tránsito.
  - Implementar programas de participación ciudadana en la planificación y evaluación de las políticas de seguridad vial.
