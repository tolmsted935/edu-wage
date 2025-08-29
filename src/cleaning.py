import pandas as pd

# Step 1: Read in Raw PUMAS Data
df = pd.read_csv("data/raw/pumas_2023.gz",low_memory=False)

# Step 2: Filter to Working Adults

df = df[(df['AGE'] >= 25) & (df['AGE'] <= 64)]   # ages 25–64
df = df[df['EMPSTAT'] == 1]                      # employed only
df = df[df['INCWAGE'] > 0]                       # positive wage

# Step 5: Save Cleaned Data
df.to_csv("data/clean/pumas_clean_2023.csv", index=False)

