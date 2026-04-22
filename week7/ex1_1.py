import pandas as pd
import time
import subprocess
import os

zip_path = "data/2023_01.csv.zip"
csv_name = "2023_01.csv"

# Unzip first, then read CSV
start = time.time()
subprocess.run(["unzip", "-o", zip_path, "-d", "data/"], check=True)
df1 = pd.read_csv(f"data/{csv_name}")
time_unzip = time.time() - start
print(f"Approach 1 (unzip + read_csv): {time_unzip:.4f} s")

# Clean up extracted file
os.remove(f"data/{csv_name}")

# Read zip directly
start = time.time()
df2 = pd.read_csv(zip_path)
time_direct = time.time() - start
print(f"Approach 2 (read_csv on zip): {time_direct:.4f} s")

faster = "Approach 1" if time_unzip < time_direct else "Approach 2"
print(f"\n{faster} is faster.")