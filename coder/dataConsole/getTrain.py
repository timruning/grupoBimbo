import pandas as pd
for i in range(ord('a'),ord('k')+1):
    df = pd.read_csv("/home/timruning/kaggle/maximize/coder/xa"+chr(i)+'1')
    lis=df["Semana"].unique()
    print lis
    for var in lis:
        dfvar = df.loc[df['Semana']==var]
        fdfvar = pd.read_csv('/home/timruning/kaggle/maximize/coder/data/train'+str(var))
        fdfvar = pd.concat([fdfvar,dfvar],ignore_index=True)
        fdfvar.to_csv('/home/timruning/kaggle/maximize/coder/data/train'+str(var),index=False)


