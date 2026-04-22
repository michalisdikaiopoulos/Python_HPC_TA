import sys

import pandas as pd
import pyarrow.csv as csv
import pyarrow.parquet as pq

fname = sys.argv[1]
df = csv.read_csv(fname)
pq.write_table( df, f"{fname}.pq")