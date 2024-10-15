import pandas as pd
df=pd.read_csv("data/test/test.csv",index_col=0)
print(df['Age'].unique())
df_train=pd.read_csv('data/train/train.csv',index_col=0)
print(df_train['Age'].unique())