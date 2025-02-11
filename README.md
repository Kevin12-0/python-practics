# Python Cpacitacion IDS

<h2>Numpy</h2>
<p>Libreia credad ampliamente usada en la computacion cientifica y el analisis de datos</p>
<p>Creada en 2005</p>
<p>Estructura las bases de datos para entender la evolucion hacia Pandas</p>
<p>Contiene objetos basicos colo los arreglos o vectores</p>

<h1> Selection for ID</h1>

```python
import numpy as np

import pandas as pd

data = {'id': [1, 2, 3, 4, 5], 'columna1': [10, 20, 30, 40, 50], 'columna2': ['A', 'B', 'C', 'D', 'E']}

df = pd.DataFrame(data)

fila_4 = df.loc[4]
```

<h1>Abrir un archivo de exel</h1>

```python
import pandas as pd

df = pd.read_excel('tu_archivo.xlsx')

print(df.head())
```

<h1>Abrir un archivo CSV</h1>

```python
import pandas as pd

df = pd.read_csv('tu_archivo.csv')

print(df.head())
```

<h1>Crear un archivo df de dimencion 10x10</h1>

```python
import pandas as pd

import numpy as np

data = np.random.randint(0, 101, size=(10, 10))

df = pd.DataFrame(data)

print(df)
```

## Elimir una columna de un dataframe

```python
import pandas as pd

df = df.drop('columna_a_eliminar', axis=1)
```

## Elimir una el id n

```python
import pandas as pd

df = df.drop(5)
```

## exportar a csv

```python
import pandas as pd

df.to_csv('datos.csv', index=False)
```
