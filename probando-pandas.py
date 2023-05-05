import pandas as pd

data = pd.read_excel('datos.xlsx', sheet_name='datos')

print(data)

nueva_fila = pd.DataFrame({'usuario':['noobmaster'], 'tengo':['si']})
data = data.append(nueva_fila, ignore_index=True)

print(data)