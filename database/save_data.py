import sqlite3
from datetime import datetime

def guardar_datos(temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo):
    conn = sqlite3.connect('riego_automatizado.db')
    c = conn.cursor()
    
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    c.execute('''
        INSERT INTO sensores (fecha_hora, temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (fecha_hora, temperatura, humedad_relativa, precipitacion, hora_del_dia, humedad_suelo))
    
    conn.commit()
    conn.close()

# Ejemplo de uso
guardar_datos(25.0, 60.0, 0.0, 14, 28.0)
