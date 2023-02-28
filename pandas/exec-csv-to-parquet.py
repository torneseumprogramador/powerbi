# pip install pyarrow

import pandas as pd
df = pd.read_csv('dados.csv')
df.to_parquet('dados.parquet', engine='pyarrow')