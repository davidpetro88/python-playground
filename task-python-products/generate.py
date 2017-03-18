import pandas as pd
import numpy as np
import random
import names

df = pd.DataFrame(columns=('code', 'piece', 'description','quantity','price'))
for i in list(range(50)):
    df.loc[i] = [i+1,names.get_first_name(),names.get_full_name(), random.randint(1, 1000), random.randint(20, 400)]

cols =['code', 'quantity']
df[cols] = df[cols].applymap(np.int64)

print(df.to_string())
df.to_csv("csv/outputProduct.csv",index=False)
