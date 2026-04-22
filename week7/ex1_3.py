import pandas as pd

def df_memsize(df):
    return df.memory_usage(deep=True).sum()

def summarize_columns(df):
    print(pd.DataFrame([
        (
            c,
            df[c].dtype,
            len(df[c].unique()),
            df[c].memory_usage(deep=True) // (1024**2)
        ) for c in df.columns
    ], columns=['name', 'dtype', 'unique', 'size (MB)']))
    print('Total size:', df.memory_usage(deep=True).sum() / 1024**2, 'MB')

zip_path = "data/2023_01.csv.zip"
df = pd.read_csv(zip_path)

df["created"] = pd.to_datetime(df["created"])
df["observed"] = pd.to_datetime(df["observed"])

df['parameterId'] = df['parameterId'].astype('category')

df['stationId'] = df['stationId'].astype('uint16')

df['value'] = df['value'].astype('float32')

df['coordsx'] = df['coordsx'].astype('category')
df['coordsy'] = df['coordsy'].astype('category')

summarize_columns(df)