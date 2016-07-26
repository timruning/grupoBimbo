import pandas as pd

def get_pruduct_agg(cols):
    df_train=pd.read_csv("/home/timruning/kaggle/maximize/kaggle/train.csv",usecols=['Semana','Producto_ID']+cols,
                         dtype={
                             "Semana":'int32',
                             'producto_ID':'int32',
                             'Venta_hoy':'float32',
                             'Venta_uni_hoy':'int32',
                             'Dev_uni_proxima':'int32',
                             'Dev_proxima':'float32',
                             'Demanda_uni_equil':'int32'
                         }
                         )
    agg=df_train.groupby(['Semana','Producto_ID'],as_index=False).agg(['count',
                                                                       'sum','min','max','median','mean'])
    agg.columns=['_'.join(col).strip() for col in agg.columns.values]
    del(df_train)
    return agg
agg1=get_pruduct_agg(['Demanda_uni_equil','Dev_uni_proxima'])
print agg1.shape
print agg1.head()
agg2=get_pruduct_agg(['Venta_uni_hoy'])
agg=agg1.join(agg2)

