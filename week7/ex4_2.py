import time
import pandas as pd

def total_precip(df):
    total = df.apply(
        lambda row: (
            row['value'] if row['parameterId'] == 'precip_past10min' else 0.0
        ),
        axis=1
    ).sum()
    return total

df = pd.read_parquet("data/2023_01.csv.pq")

# Subsample to avoid waiting forever
df_sample = df.sample(n=100000, random_state=42)

start = time.time()
result = total_precip(df_sample)
elapsed = time.time() - start

print(f"Result: {result:.4f}")
print(f"Time (n=100,000): {elapsed:.4f} s")

# Extrapolate to full dataset
full_estimate = elapsed * (len(df) / len(df_sample))
print(f"Estimated time for full dataset ({len(df)} rows): {full_estimate:.1f} s")


# ----------------- ESTIMATED TIME: 0.47sec -----------------