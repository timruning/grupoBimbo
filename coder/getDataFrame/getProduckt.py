import pandas as pd
products=pd.read_csv("/home/timruning/kaggle/maximize/kaggle/producto_tabla.csv")
print products.head()
products['short_name']=products.NombreProducto.str.extract('^(\D*)',expand=False)
products['brand']=products.NombreProducto.str.extract('^.+\s(\D+) \d+$',expand=False)
w=products.NombreProducto.str.extract('(\d+)(Kg|g)',expand=True)
products['weight']=w[0].astype('float')*w[1].map({'Kg':1000,'g':1})
products['pieces']=products.NombreProducto.str.extract('(\d+)p ',expand=False).astype('float')
print '-----------------------------'
print  products.head()
print  products.tail()
print products.short_name.value_counts(dropna=False)
