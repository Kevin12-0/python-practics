# Python Cpacitacion IDS

<h2>Numpy</h2>
<p>Libreia credad ampliamente usada en la computacion cientifica y el analisis de datos</p>
<p>Creada en 2005</p>
<p>Estructura las bases de datos para entender la evolucion hacia Pandas</p>
<p>Contiene objetos basicos colo los arreglos o vectores</p>

<h1>Seleccionar por id</h1>
````python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'id': [1, 2, 3, 4, 5],
        'columna1': [10, 20, 30, 40, 50],
        'columna2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

# Seleccionar la fila con el ID 4 utilizando diferentes métodos
fila_4_por_etiqueta = df.loc[4]
fila_4_por_condicion = df[df['id'] == 4]
fila_4_por_posicion = df.iloc[3]  # La posición 3 corresponde a la cuarta fila

print(fila_4_por_etiqueta)
print(fila_4_por_condicion)
print(fila_4_por_posicion)```
