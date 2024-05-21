import joblib
import requests
import pandas as pd
import sqlite3
from datetime import datetime

# Cargar modelo
model = joblib.load('modelo_riego.pkl')

# Obtener datos actuales del sensor y clima (esto debería ser reemplazado por datos en tiempo real)
datos_actuales = {
    'temperatura': 25,  # Ejemplo de temperatura
    'humedad_relativa': 60,  # Ejemplo de humedad relativa
    'precipitacion': 0,  # Ejemplo de precipitación
    'hora_del_dia': 14  # Ejemplo de hora del día (14:00)
}

# Convertir datos a formato adecuado
datos_df = pd.DataFrame([datos_actuales])

# Predecir nivel de humedad
humedad_predicha = model.predict(datos_df)[0]

# Determinar si se debe regar
umbral_humedad = 30  # Nivel de humedad mínimo antes de activar el riego

if humedad_predicha < umbral_humedad:
    requests.get('http://192.168.1.100/activar_riego')
    estado_riego = 'activado'
else:
    requests.get('http://192.168.1.100/desactivar_riego')
    estado_riego = 'desactivado'

# Guardar datos en la base de datos
def guardar_datos(temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo, estado_riego):
    conn = sqlite3.connect('riego_automatizado.db')
    c = conn.cursor()
    
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    c.execute('''
        INSERT INTO sensores (fecha_hora, temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo, estado_riego)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (fecha_hora, temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo, estado_riego))
    
    conn.commit()
    conn.close()

guardar_datos(datos_actuales['temperatura'], datos_actuales['humedad_relativa'], datos_actuales['precipitacion'], datos_actuales['hora_del_dia'], humedad_predicha, estado_riego)

