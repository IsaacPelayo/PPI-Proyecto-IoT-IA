import sqlite3

def obtener_datos():
    conn = sqlite3.connect('riego_automatizado.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM sensores')
    datos = c.fetchall()
    
    conn.close()
    return datos

# Ejemplo de uso
datos = obtener_datos()
for dato in datos:
    print(dato)
