import pandas as pd
import numpy as np

# ── Step 1: Load data ──────────────────────────────
df = pd.read_csv('C:/Users/tuf/OneDrive/Attachments/Desktop/projects for data analyst/superstore-sales-dashboard/data/superstore.csv', encoding='latin-1')
print("Shape:", df.shape)
print(df.head())

# ── Step 2: Fix column names ───────────────────────
df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
print("\nColumns:", df.columns.tolist())

# ── Step 3: Fix data types ─────────────────────────
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=False)
df['ship_date']  = pd.to_datetime(df['ship_date'],  format='mixed', dayfirst=False)
print("\nData types:\n", df.dtypes)

# ── Step 4: Check missing values ───────────────────
print("\nMissing values:\n", df.isnull().sum())
df = df.dropna(subset=['sales', 'profit', 'order_date'])
df['postal_code'] = df['postal_code'].fillna('Unknown')

# ── Step 5: Remove duplicates ──────────────────────
print("\nDuplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# ── Step 6: Remove bad data ────────────────────────
df = df[df['sales'] > 0]

# ── Step 7: Add new columns ────────────────────────
df['profit_margin']     = round((df['profit'] / df['sales']) * 100, 2)
df['order_month']       = df['order_date'].dt.month
df['order_year']        = df['order_date'].dt.year
df['order_month_name']  = df['order_date'].dt.strftime('%B')
df['shipping_days']     = (df['ship_date'] - df['order_date']).dt.days

# ── Step 8: Save clean data ────────────────────────
df.to_csv('superstore_clean.csv', index=False)
print("\nDone! Final shape:", df.shape)
print(df[['order_date','sales','profit','profit_margin','shipping_days']].head())
