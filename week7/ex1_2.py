import pandas as pd

def df_memsize(df):
    return df.memory_usage(deep=True).sum()

zip_path = "data/2023_01.csv.zip"
df = pd.read_csv(zip_path)

print(f"The size of the dataframe is {df_memsize(df) / 1024 ** 2} MB")