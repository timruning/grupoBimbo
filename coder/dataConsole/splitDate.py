import pandas as pd
# xab1=pd.read_csv("/home/timruning/kaggle/maximize/coder/xab1")
# print xab1.head()
# print xab1['Semana'].unique()
for i in range(3,10):
    traini=pd.DataFrame(columns=('Semana','Agencia_ID','Canal_ID','Ruta_SAK','Cliente_ID','Producto_ID',
                                 'Venta_uni_hoy','Venta_hoy','Dev_uni_proxima','Dev_proxima','Demanda_uni_equil'))
    traini.to_csv("/home/timruning/kaggle/maximize/coder/data/train"+str(i),index=False)
