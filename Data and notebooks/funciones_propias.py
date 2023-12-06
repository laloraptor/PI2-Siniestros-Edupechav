import pandas as pd
import numpy as np
import requests
from unidecode import unidecode
import re

def sin_limites():
    # Desactivar la limitación de visualización
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

def limitar():
    # Reactivar la limitación de visualización
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')

# Formatear nombre a Nombre_Nombre en df
def format_nombres(df):
    df.columns = df.columns.str.title().str.replace(' ', '_')

# Explorar y eliminar filas duplicadas en df
def eliminar_duplicadas(df):
    filas_duplicadas = df.duplicated()
    cantidad_duplicadas = filas_duplicadas.sum()

    if cantidad_duplicadas > 0:
        print("Filas duplicadas:")
        print(df[filas_duplicadas])
        
        eliminar = input(f"\n¿Deseas eliminar las filas duplicadas? (Sí/No): ").strip().lower()

        if eliminar == 'si' or eliminar == 's':
            df_sin_duplicadas = df.drop_duplicates()
            print("\nFilas duplicadas eliminadas.")
            return df_sin_duplicadas
        else:
            print("\nNo se eliminaron las filas duplicadas.")
            return df
    else:
        print("No hay filas duplicadas.")
        return "nada por eliminar"

#Explorar tipos de valores en columnas del df
def tipos_cols(df):
    resultados = []

    for columna in df.columns:
        tipos_de_valor = df[columna].apply(type).unique()
        cantidad_de_tipos = len(tipos_de_valor)

        tipos_valor_cantidad = dict(zip(tipos_de_valor, df[columna].apply(lambda x: str(type(x))).value_counts()))

        # Agregar información sobre valores perdidos
        cantidad_valores_perdidos = df[columna].isnull().sum()
        tipos_valor_cantidad[np.nan] = cantidad_valores_perdidos

        for tipo, cantidad in tipos_valor_cantidad.items():
            resultado_columna = {
                'Columna': columna,
                'Tipo de Valor': tipo,
                'Cantidad': cantidad,
                'Más de un tipo de valor (no NaN)': 'Sí' if cantidad_de_tipos > 1 else 'No'
            }

            resultados.append(resultado_columna)

    return pd.DataFrame(resultados)

# explorar valores unicos y tipos en df

def unicos_col(df_columna):
    resumen = pd.DataFrame(columns=['tipo', 'conteo', 'valores'])

    tipos_clases = df_columna.apply(type).unique()

    for tipo_clase in tipos_clases:
        valores_unicos = df_columna[df_columna.apply(type) == tipo_clase].unique().tolist()
        conteo = len(valores_unicos)

        resumen.loc[len(resumen)] = {'tipo': tipo_clase, 'conteo': conteo, 'valores': valores_unicos}

    # Imprimir la cantidad total de observaciones
    print(f'\nCantidad total de observaciones: {len(df_columna)}')

    return resumen

# Frecuencia de valores unicos 
def frecuencia_unicos(df_columna):
    frecuencia = df_columna.value_counts()
    print("Frecuencia de Valores Únicos:")
    print(frecuencia)





def transformar_calle(df_columna):
    # Reemplazar NaN con cadena vacía
    df_columna = df_columna.fillna('')

    # Normalizar caracteres especiales
    df_columna = df_columna.apply(lambda x: unidecode(str(x)))

    # Reemplazar "?" con "ñ"
    df_columna = df_columna.str.replace('?', 'ñ')

    # Cambiar el orden de las palabras y capitalizar
    df_columna = df_columna.apply(lambda x: ' '.join(word.capitalize() for word in x.split()[::-1]))

    return df_columna

# Definir la clave de API de Google Maps
api_key = 'AIzaSyBy59rA1MRZhuj3FMnagwDle4XvEYjV3fI'

# Definir la base de la URL de la API de Geocoding
base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Definir una función que reciba un dataframe con las columnas Pos_X y Pos_Y
def convertir_coordenadas(df):
  # Crear una lista vacía para almacenar las direcciones
  direcciones = []

  # Iterar por cada fila del dataframe
  for index, row in df.iterrows():
    # Obtener las coordenadas de las columnas Pos_X y Pos_Y
    lat = row['Pos_X']
    lng = row['Pos_Y']

    # Construir el parámetro de coordenadas para la URL
    coord = f'{lat},{lng}'

    # Construir la URL completa con la clave de API y el parámetro de coordenadas
    url = base_url + 'key=' + api_key + '&latlng=' + coord

    # Hacer la petición HTTP a la API y obtener la respuesta en formato JSON
    response = requests.get(url).json()

    # Verificar si la respuesta tiene el estado 'OK'
    if response['status'] == 'OK':
      # Obtener la primera dirección de los resultados
      direccion = response['results'][0]['formatted_address']

      # Añadir la dirección a la lista
      direcciones.append(direccion)
    else:
      # Si la respuesta no tiene el estado 'OK', añadir un valor vacío a la lista
      direcciones.append('')

  # Añadir la lista de direcciones como una nueva columna al dataframe
  df['Direccion'] = direcciones

  # Devolver el dataframe modificado
  return df

