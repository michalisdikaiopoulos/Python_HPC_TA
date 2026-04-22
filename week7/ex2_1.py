from pyarrow import csv
import pyarrow as pa
import time

start = time.time()

import subprocess
subprocess.run(["unzip", "-o", "data/2023_01.csv.zip", "-d", "data/"], check=True)

convert_options = csv.ConvertOptions(
    column_types={
        'value': pa.float32(),
        'parameterId': pa.dictionary(pa.int32(), pa.string()),
        'coordsx': pa.dictionary(pa.int32(), pa.float64()),
        'coordsy': pa.dictionary(pa.int32(), pa.float64()),
    }
)

table = csv.read_csv("data/2023_01.csv", convert_options=convert_options)
df = table.to_pandas()
elapsed = time.time() - start

print(f"PyArrow load + convert to pandas: {elapsed:.4f} s")