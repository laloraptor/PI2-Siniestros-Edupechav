# **EPC. EDA. Segundo proyecto**

En este apartado se lleva a cabo el análisis exploratorio de los datos

## 0. Preparativos

Importar la base que resultó del ETL y las librerías necesarias para este apartado

Obtenemos la información general de la base

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 704 entries, 0 to 703
    Data columns (total 26 columns):
     #   Column                    Non-Null Count  Dtype         
    ---  ------                    --------------  -----         
     0   Id                        704 non-null    object        
     1   N_Victimas                704 non-null    int64         
     2   Fecha_Siniestro           704 non-null    datetime64[ns]
     3   Hora                      704 non-null    object        
     4   Lugar_Del_Hecho           704 non-null    object        
     5   Tipo_De_Calle             704 non-null    object        
     6   Comuna                    704 non-null    int64         
     7   Pos_X                     704 non-null    float64       
     8   Pos_Y                     704 non-null    float64       
     9   Victima                   704 non-null    object        
     10  Acusado                   704 non-null    object        
     11  Barrios                   704 non-null    object        
     12  Rol                       704 non-null    object        
     13  Sexo                      704 non-null    object        
     14  Edad                      704 non-null    int32         
     15  Fecha_Fallecimiento       704 non-null    datetime64[ns]
     16  Semestre                  704 non-null    int64         
     17  Hora_Siniestro            704 non-null    int64         
     18  Anio_Siniestro            704 non-null    int32         
     19  Mes_Siniestro             704 non-null    int32         
     20  Dia_Siniestro             704 non-null    int32         
     21  Anio_Fallecimiento        704 non-null    int32         
     22  Mes_Fallecimiento         704 non-null    int32         
     23  Dia_Fallecimiento         704 non-null    int32         
     24  Dia_Semana_Siniestro      704 non-null    object        
     25  Dia_Semana_Fallecimiento  704 non-null    object        
    dtypes: datetime64[ns](2), float64(2), int32(7), int64(4), object(11)
    memory usage: 123.9+ KB
    

## 1. Estadísticas descriptivas

Vamos a utilizar copia de df para no alterar los datos para los gráficos posteriores

### 1.1. Variables tratadas como numéricas

Vamos a utilizar las variables siguientes para obtener el valor esperado (la media), la variación de ese valor y cómo se distribuyen.

    Estadísticas Descriptivas para Columnas Numéricas:
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>N_Victimas</th>
      <th>Edad</th>
      <th>Hora_Siniestro</th>
      <th>Anio_Siniestro</th>
      <th>Anio_Fallecimiento</th>
      <th>Mes_Siniestro</th>
      <th>Dia_Siniestro</th>
      <th>Mes_Fallecimiento</th>
      <th>Dia_Fallecimiento</th>
      <th>Dia_Semana_Siniestro</th>
      <th>Dia_Semana_Fallecimiento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
      <td>704.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.059659</td>
      <td>42.276989</td>
      <td>11.551136</td>
      <td>2018.186080</td>
      <td>2018.193182</td>
      <td>6.690341</td>
      <td>15.940341</td>
      <td>6.650568</td>
      <td>15.752841</td>
      <td>4.002841</td>
      <td>3.987216</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.254391</td>
      <td>19.154496</td>
      <td>6.669836</td>
      <td>1.670863</td>
      <td>1.677280</td>
      <td>3.580907</td>
      <td>8.654215</td>
      <td>3.567285</td>
      <td>8.666985</td>
      <td>2.005680</td>
      <td>2.009538</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>2016.000000</td>
      <td>2016.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>28.000000</td>
      <td>6.000000</td>
      <td>2017.000000</td>
      <td>2017.000000</td>
      <td>3.750000</td>
      <td>9.000000</td>
      <td>3.000000</td>
      <td>9.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>39.000000</td>
      <td>11.000000</td>
      <td>2018.000000</td>
      <td>2018.000000</td>
      <td>7.000000</td>
      <td>16.000000</td>
      <td>7.000000</td>
      <td>16.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.000000</td>
      <td>55.000000</td>
      <td>17.000000</td>
      <td>2019.000000</td>
      <td>2019.000000</td>
      <td>10.000000</td>
      <td>23.000000</td>
      <td>10.000000</td>
      <td>23.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>95.000000</td>
      <td>23.000000</td>
      <td>2021.000000</td>
      <td>2022.000000</td>
      <td>12.000000</td>
      <td>31.000000</td>
      <td>12.000000</td>
      <td>31.000000</td>
      <td>7.000000</td>
      <td>7.000000</td>
    </tr>
  </tbody>
</table>
</div>



El número promedio de víctimas fatales por siniestro es de 1.06, con una desviación estándar baja de 0.25; esto implica poca variabilidad y datos altamente concentrados alrededor de 1, como confirma el valor del tercer cuartil que también es 1.

La edad promedio de los fallecidos es 42 años, con desviación de 19 años, sugiriendo una dispersión moderada en las edades. El valor del primer y tercer cuartil (28 y 55 años) ratifica la existencia de cierta variabilidad etaria, pero con concentración en adultos de mediana edad

En cuanto a la hora del incidente, se observa un promedio de 11.55 horas, es decir, cerca del mediodía. La desviación estándar es de 6.7 horas, significativamente alta, lo cual señala una distribución extendida a lo largo del día, sin concentración horaria específica. El año del siniestro muestra un promedio de 2018 con con una desviación (baja) de 1.67 años, esto se debe a que los datos temporalmente proporcionados son acotados y poco dispersos.

Por otro lado, la variable mes del siniestro tiene un promedio de 6.7, próximo a julio, con desviación moderada de 3.6 meses, sugiriendo fluctuación no extrema en esta dimensión temporal. De forma similar, el día del siniestro promedia los 16 días del mes, y presenta una alta variabilidad. Finalmente, el día de la semana del siniestro tiene un valor medio cercano al miércoles (4 en la escala), con desviación de 2 días, ratificando fluctuación acotada en este atributo categórico.

#### 1.1.1. Valores atipicos

A continuación vamos a buscar valores atipicos. Este paso es casi omitible debido a que de antemano sabemos que las columnas tienen valores de rangos muy conocidos y limitados (no puede haber una observación con mes 50 o día 40, por ejemplo).


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_17_0.png)
    


En este caso los gráficos nos sirven para observar que los datos tienen escalas muy distintas. Hay "outliers" en el Número de victimas, pero ocurre sólo porque, como vimos en los descriptivos, el 75% de los datos tiene 1 como valor. Aunque no lo parece, saber que las escalas son distintas será útil para pensar en transformar los datos para compararlos en escalas comunes y encontrar correlaciones.  

### 1.2 Variables tratadas como categóricas

Pasamos ahora a observar las columnas que mantuvimos como categóricas. En este caso nos concentraremos en ver el top 5 (o menos) de aquellas categorías con mayor frecuencia.

    
    Cuenta de Valores Únicos para Columnas Categóricas:
    
    Top 5 Frecuencias para Sexo:
    2    536
    1    166
    3      2
    Name: Sexo, dtype: int64
    
    Top 5 Frecuencias para Tipo_De_Calle:
    AVENIDA      510
    CALLE        136
    AUTOPISTA     58
    Name: Tipo_De_Calle, dtype: int64
    
    Top 5 Frecuencias para Comuna:
    1    93
    4    76
    9    72
    8    67
    7    61
    Name: Comuna, dtype: int64
    
    Top 5 Frecuencias para Victima:
    Moto         294
    Peaton       263
    Auto          91
    Bicicleta     29
    Sd             8
    Name: Victima, dtype: int64
    
    Top 5 Frecuencias para Acusado:
    Auto           208
    Pasajeros      177
    Cargas         144
    Objeto Fijo     66
    Moto            58
    Name: Acusado, dtype: int64
    
    Top 5 Frecuencias para Rol:
    CONDUCTOR               323
    PEATON                  264
    PASAJERO_ACOMPAÑANTE     79
    CICLISTA                 29
    SD                        9
    Name: Rol, dtype: int64
    
    Top 5 Frecuencias para Semestre:
    2    365
    1    339
    Name: Semestre, dtype: int64
    

En primer lugar, se observa que son hombres quienes están involucrados en la mayor cantidad de siniestros viales como victimas.

En Tipo de calle predomina ampliamente la categoría "Avenida" con 511 casos, seguida por "Calle" con 138. Para la variable Comuna destacan los valores 1, 4, 9, 8 y 7, en éstas comunas ocurren entre 62-93 casos; de manera más específica  la comuna No. 1 destaca un poco del resto.

En cuanto a Víctima, se observa que la mayor cantidad de siniestros le ocurren a personas que conducen motocicletas (302 registros), seguida por "Peatón" con 266. Mientras la variable acusado muestra que el probable responsable es mayoritariamente un conductor de auto (210).

Por su parte, la variable Rol muestra que la mayor cantidad de siniestros ocurren a las personas mientras conducen (330) y en segundo lugar mientras transitan por la calle "Peatón" (267). Finalmente, para Semestre se observa una frecuencia ligeramente mayor en el segundo semestre con 370 casos versus 347 del primero.

## 2. Graficos generales

### Distribución de edad por sexo


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_25_0.png)
    


La gráfica muestra la distribución por edad y género de las víctimas. Se observa que los hombres jóvenes entre 20 y 40 años son los más afectados, con un valor modal claramente remarcado en los 40 años. En contraste, en las mujeres la mayor frecuencia se da entre los 40 y 60 años. Esto sugiere patrones diferentes en que hombres y mujeres se ven involucrados en siniestros viales. Resalta con claridad el hecho de que en los hombres la frecuencia de incidentes disminuye con la edad, mientras que en las mujeres se mantiene relativamente estable.


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_27_0.png)
    


Respecto al número de victimas. Como habíamos visto en estadisticos anteriores, casi la totalidad de los incidentes involucran una sola víctima. Un porcentaje muy reducido involucran a más de dos y los incidentes con más de tres víctimas son casi inexistentes en el caso de los hombres y nulos en el caso de las mujeres. Aunque lo cierto es que cada fila de los datos indica una única categoría de sexo en vez de las posibles combinaciones de las víctimas; sería necesario ahondar más para saber si, en el conteo, necesariamente todas las víctimas reportadas son del mismo sexo.

### Distribución espacial

    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\288541281.py:18: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.
      colores_comunas = plt.cm.get_cmap('Pastel1', len(comunas))
    


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_30_1.png)
    



    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_31_0.png)
    


A partir de la representación espacial y del gráfico de barras se puede notar que hay 5 comunas que concentran significativamente más victimas que otras: se trata de las comunas 1,4, 9, 8 y 7. No parece haber un patrón claro en torno a la región en que suceden los incidentes.


### Distribución temporal: año, mes y día


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_34_0.png)
    


Respecto a la distribución tempora, en primer lugar se aprecia gran concordancia entre las fechas en que ocurrieron los siniestros y las fechas de fallecimiento (esto se discutirá con mayor detalle más adelante). Por otro lado, a nivel de año se aprecian fluctiaciones sin un patrín muy claro quizñas hasta 2020, y en el que destacan algúnos momentos específicos. Por ejemplo se nota que Enero y junio de 2017, así como enero de 2021 fueron momentos en que la frecuencia de los siniestros fue muy distinta al resto del periodo analizado. Esto podría indicar eventos anormales. En el caso del pico de 2021 es posible notar una tendencia a la baja durante 2020 que, quitando el pico observado, continúo durante 2021; misma que podría deberse al confinamiento durante la pandemia de COVID, el cual redujo el tránsito de las personas a través de diversos medios. El pico podría estar relacionado con el aumento de salidas por las fiestas decembrinas, y la identidad entre la cantidad de siniestros y fallecimientos podría deberse a la saturación de hospitales en ese mes.


La segunda gráfica sugiere la presencia de patrones estacionales, como se evidencia por los aumentos y disminuciones periódicos en el número de siniestros y fallecimientos a lo largo de los meses. Ambos: siniestros y fallecimientos parecen tener un pico significativo hacia el final del año (mes 12), lo que podría indicar una tendencia estacional o un evento específico que conduzca a un aumento en estos incidentes (como la existencia de vaciones o la urgencia de reuniones por fiestas compartidas).

La gráfica muestra que el porcentaje de accidentes y muertes fluctúa a lo largo del mes, con algunos picos y valles. Los picos más altos están en los días 17 y 20, mientras que las caídas ocurren en el día 8 y 31. La caída del día 31 se explica por la disminución en la cantidad de meses que tienen ese número de días, mientras que no hay una respuesta que, a priori, parezca clara para explicar la caída del día 8.  

## 3. Matriz de correlación para orientar revisión específica

Para orientar la revisión de "interacciones específicas" se va a realizar primero una matriz de correlación.
Debido a que el rango de las variables continuas varía bastante es necesario aplicar una transformación logarítmica para alinear las escalas numéricas a proporciones comparables y realizar correctamente la matriz de correlación, esto con el fin de intentar descubrir relaciones valiosas entre los datos.

La transformación es necesaria porque, por ejemplo, hay variables como el número de víctimas que originalmente presentan diferencias absolutas pequeñas entre sus valores extremos (de 1 a 3 víctimas). Sin embargo, estas diferencias absolutas no reflejan adecuadamente que el valor máximo es apenas tres veces más grande que el mínimo; mientras que, en la variable "Mes" la diferencia entre los valores mínimo y máximo (1 a 12) es bastamte más amplia en términos de su propia escala, situación que ocurre con las demás variables también. Es así que la transformación permite que las correlación entre variables se realice entre escalas con proporciones comparables.


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_38_0.png)
    


Fuera de las correlaciones obvias (fallecimientos y siniestros) hay correlaciones que, si bien bajas, dan insights sobre algunos factores que pueden afectar la variabilidad del número de victimas. Podemos destacar lo siguiente:

En primer lugar, se observa una correlación negativa débil entre el número de víctimas y la edad (-0.096). Esto podría sugerir que los siniestros con mayor número de víctimas tienden a involucrar a personas más jóvenes. Ahondar en cómo varía la cantidad de víctimas entre diferentes rangos etarios puede arrojar más luz sobre esta relación.

También se aprecia una correlación negativa similar entre víctimas y hora del siniestro (-0.099). Esto podría indicar que ciertas franjas horarias están asociadas a una mayor probabilidad de siniestros con múltiples fallecidos. Analizar en detalle este factor temporal sería revelador para entender mejor este vínculo.  

En otro orden, existe una correlación positiva moderada (0.118) entre el número de víctimas y el día de la semana. Esto sugiere que la mortalidad puede fluctuar significativamente dependiendo del día en que ocurre el incidente. Desagregar por días específicos llevaría a comprender mejor cómo se relacionan estas dos variables.

Adicionalmente, hay una correlación positiva entre edad y hora del siniestro (0.176), indicando que el perfil etario parece variar según horario del siniestro. También se halló correlación negativa entre edad y sexo (-0.199), sugiriendo la existencia de diferencias demográficas de género que pueden ser relevantes para el análisis.

En resumen, la matriz de correlaciones permite identificar varias relaciones entre atributos que ameritan una investigación más exhaustiva mediante análisis gráficos, estadísticos y otros procedimientos. Seguir explorando estos vínculos tentativos será clave para obtener insights más profundos.

A continuación comenzaremos por analizar las relaciones descubiertas en este punto



## 4. Gráficos específicos

### Víctimas por días de la semana, segmento del día  y categorías de edad

    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\4159041466.py:12: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_dia = df_siniestros.groupby('Dia_Semana_Siniestro').size() / len(df_siniestros) * 100
    


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_44_1.png)
    


    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\4159041466.py:34: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_hora = df_siniestros.groupby('Hora_Categoria').size() / len(df_siniestros) * 100
    


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_44_3.png)
    


La primera "Porcentaje de víctimas por día de la semana y categoría de edad" muestra el porcentaje de incidentes por día (el texto en la parte baja de las barras), donde se puede notar que la cantidad de incidentes no es muy distinta entre días de la semana, pues cada día concentra entre el 13 y el 15% de los incidentes. Sin embargo, al desagregar el porcentaje de incidentes en función de las categorías de edad que se crearon para este análisis, es posible obtener información que ya no es tan homogenea.

En primar lugar sobresale el hecho de que el grupo de 25 a 45 años es el que experimenta la mayor cantidad de incidentes mortales. Del mismo modo, en conjunto con el grupos de 15-24 años muestran picos más pronunciados durante el fin de semana; por su parte, al grupo de 60 años y más le ocurren más accidentes entre semana.

 En la segunda gráfica, "Porcentaje de incidentes por segmento del día", se observa que las personas entre 25 y 45 años tienen la mayor cantidad de incidentes durante la madrugada y la mañana. Mientras que el grupo de mayores de 60 años tiene el mayor porcentaje de víctimas por la tarde.

 Las tendencias podrían reflejar patrones de comportamiento social y actividad de los diferentes grupos de edad, como la vida nocturna, el trabajo, la escuela, o la exposición a diferentes riesgos en distintos momentos.

    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\3790014627.py:26: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_hombres = df_masculino.groupby('Dia_Semana_Siniestro').size() / len(df_masculino) * 100
    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\3790014627.py:40: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_mujeres = df_femenino.groupby('Dia_Semana_Siniestro').size() / len(df_femenino) * 100
    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\3790014627.py:57: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_hombres_hora = df_masculino.groupby('Hora_Categoria').size() / len(df_masculino) * 100
    C:\Users\Eduardo\AppData\Local\Temp\ipykernel_11348\3790014627.py:74: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      porcentaje_mujeres_hora = df_femenino.groupby('Hora_Categoria').size() / len(df_femenino) * 100
    


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_46_1.png)
    


Al desagregar los datos anteriores por sexo se encuentran hallazgos importantes.

Para los hombres, el mayor porcentaje de víctimas se presenta en el grupo de 25-45 años, especialmente hacia el final de la semana (sábado, domingo y lunes).

En las mujeres, el grupo de 25-45 años también muestra un pico los días sábado y domingo, pero con un porcentaje significativamente menor en comparación con los hombres. Sin embargo, lo más sobresaliente es que, en el caso de las mujeres, el grupo más expuesto a siniestros es el de personas mayores

Por otro lado, respecto a las diferencias por incidentes a lo largo del día, los hombres mantienen la tendencia general de la gráfica anterior, con el porcentaje de cada momento del día muy cercando entre sí; sin embargo, las mujeres se distancian de esa tendencia; pues muestran estar más expuestas a incidentes durante la mañana y durante la tarde, estos momentos concentral el 65% de las ocurrencias.  

### Tipos de Victimas, Acusados y Roles, por sexo


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_49_0.png)
    



    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_49_1.png)
    



    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_49_2.png)
    


La gráfica de victima por sexo muestra una diferencia clara en el tipo de incidentes mortales que más afectan a hombres y a mujeres. En el caos de los primeros, prácticamente la mitad de los sucesos les ocurren mientras conducen una motocicleta, mientras que a las mujeres les ocurren mientras caminan por la calle. Es por esta razón que, se elige tomar la reducción de los siniestros que involucran a mujeres (en calidad de peaton) como un kpi indispensable.

Por su parte, la gráfica de Acusados por sexo, otorga información complementaria a la anterior. En ambos caso, tanto hombres como mujeres, son en su mayoría víctimas de automoviles y pasajeros.

Finalmente, la gráfica de "Rol por sexo", complementa mejor a la de tipos de víctimas. En este caso, se añade la información de que las mujeres tienen muchos más incidentes siendo pasajeras que los hombres

### Víctima vs acusado, frecuencias


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_52_0.png)
    


Se observa que hay algunas frecuencias más altas que otras en cuanto a la combinación de Acusados y Víctimas. Los autos y cargas generan más siniestros sobre Motos y peatones, aunque, sorpresivamente son los pasajeros quienes generan más siniestros en Peatones que cualquier otro acusado

### Tipo de calle por sexo


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_55_0.png)
    


Respecto al tipo de calle, se observan algunas diferencias que son congruentes con los resultados anteriores. Las mujeres, que en su mayoría tienen incidentes siendo  peatones, tienen 7pp más de incidentes sobre calles que los hombres. Mientras que estos tienen 6pp más de incidentes en autopistas.

### Frecuencia de Siniestros y Fallecimientos por día Días de la Semana con promedio de días de diferencias entre uno y otro


    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_58_0.png)
    


Finalmente, se presenta el análisis de la comparación entre la frecuencia de siniestros y muertes por día de la semana. En primer lugar se aprecia una clara separación entre la frecuencia de muertes por día  y la frecuencia de siniestros por día. Esto quiere decir, basicamente, que las personas que tienen incidentes mortales no mueren siempre el mismo día del incidente. La diferencia entre las frecuencias no es directamente interpretable debido a que la muerte y el siniestro se encuentran "desfasados" es por ello que se calculó el tiempo promedio en días que pasa entre el fallecimiento y el siniestro.

En este sentido la tendencia es clara. El tiempo promedio entre el siniestro y el fallecimiento es mayor de Martes a Viernes, es decir, entre semana; siendo el jueves el día con mayor diferencia. Esto puede significar dos cosas:


1.   Que los accidentes que ocurren durante la semana son "un poco menos graves", de manera que se prolonga la supervivencia un poco más. Mientras que el domingo (incluye la madrugada) y lunes, los siniestros son resultado de prácticas culturales que los vuelven más agresivos y con tiempos de supervivencia menores.

o

2.   Que el domingo y el lunes, por diversos motivos, la atención medica disminuye en calidad o capacidad, de manera que no es capaz de prolongar la vida durante más tiempo. Mientras que durante semana ocurre lo contrario.  




    
![png](2_EDA_EDP_Final_files/2_EDA_EDP_Final_60_0.png)
    


Por último, desagregando por sexo hay patrones contrastantes.

En primer lugar, el promedio de supervivencia general (en rojo, en la gráfica) muestra que el tiempo de supervivencia es un poco más corto, quizás como resultado de que gran parte de los siniestros ocurren a las mujeres el día domingo.  Del mismo modo, se aprecia que los siniestros que las involucran se distribuyen durante todda la semana, con el pico ya mencionado; mientras que, en el caso de los hombres, los incidentes van a la baja desde el día lunes, tocan el punto más inferior el miercoles y viernes y comienzan a partir de entonces. Lo que sugiere dinámicas contrastantes.


