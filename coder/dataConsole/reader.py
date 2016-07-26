import pandas as pd
# for i in range(ord('a'),ord('a')+1):
#     file=pd.read_csv("/home/timruning/kaggle/maximize/coder/xa"+chr(i)+"1")
#     print "xa"+chr(i)+"1"
#     print file.head()
for i in range(3,10):
    df=pd.read_csv("/home/timruning/kaggle/maximize/coder/data/train"+str(i))
    print df["Semana"].unique()


