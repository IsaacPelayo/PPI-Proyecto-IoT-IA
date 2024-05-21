import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Cargar datos
data = pd.read_csv('humedad_clima_datos.csv')

# Preprocesar datos
X = data[['temperatura', 'humedad_relativa', 'precipitacion', 'hora_del_dia']]
y = data['humedad_suelo']

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, 'modelo_riego.pkl')
