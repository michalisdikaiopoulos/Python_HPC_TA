import sys
import pandas as pd

# From week 7 solutions
def precip(df):
    precip = float(df[df['parameterId'] == 'precip_past10min']['value'].sum())
    return precip

if __name__ == '__main__':
    fname = sys.argv[1]
    if len(sys.argv) > 2:
        chunksize = int(sys.argv[2])
        df_chunks = pd.read_csv(
            fname,
            #usecols=['parameterId', 'value'],
            chunksize=chunksize
        )

        total = 0
        for chunk in df_chunks:
            total += precip(chunk)
    else:
        # Convenience to check without any chunking
        df = pd.read_csv(
            fname,
            #usecols=['parameterId', 'value']
        )
        total = precip(df)
    print(total)