import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('riego_automatizado.db')
c = conn.cursor()

# Crear tabla
c.execute('''
    CREATE TABLE IF NOT EXISTS sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_hora TEXT,
        temperatura REAL,
        humedad_relativa REAL,
        precipitacion REAL,
        hora_del_dia INTEGER,
        humedad_suelo REAL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
