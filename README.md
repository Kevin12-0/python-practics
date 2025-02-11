# Python Cpacitacion IDS

<h2>Numpy</h2>
<p>Libreia credad ampliamente usada en la computacion cientifica y el analisis de datos</p>
<p>Creada en 2005</p>
<p>Estructura las bases de datos para entender la evolucion hacia Pandas</p>
<p>Contiene objetos basicos colo los arreglos o vectores</p>

<h1>Seleccionar por id</h1>
```python
import pandas as pd

data = {'id': [1, 2, 3, 4, 5],
        'columna1': [10, 20, 30, 40, 50],
        'columna2': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)

fila_4_por_etiqueta = df.loc[4]
fila_4_por_condicion = df[df['id'] == 4]
fila_4_por_posicion = df.iloc[3]

print(fila_4_por_etiqueta)
print(fila_4_por_condicion)
print(fila_4_por_posicion)```


```import pandas as pd

data = {'columna1': [1, 2, None, 4],
        'columna2': [5, None, 7, 8]}
df = pd.DataFrame(data)

df = df.fillna(0)````


## leer archivo de excel

```
python
import pandas as pd

df = pd.read_excel('tu_archivo.xlsx')

print(df)```

# crear un df con dimenciones de 10x10
```
import pandas as pd
import numpy as np

data = np.random.randint(0, 101, size=(10, 10))
df = pd.DataFrame(data)

print(df)```

