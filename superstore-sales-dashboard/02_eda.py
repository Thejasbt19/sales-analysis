import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('superstore_clean.csv')

# ── Chart 1: Monthly Sales Trend ───────────────────
monthly = df.groupby(['order_year','order_month'])['sales'].sum().reset_index()
monthly['date'] = pd.to_datetime(
    monthly['order_year'].astype(str) + '-' + monthly['order_month'].astype(str) + '-01'
)
plt.figure(figsize=(12,4))
plt.plot(monthly['date'], monthly['sales'], marker='o', color='steelblue', linewidth=2)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('chart_monthly_sales.png')
plt.show()

# ── Chart 2: Sales by Category ─────────────────────
cat_sales = df.groupby('category')['sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(7,4))
cat_sales.plot(kind='bar', color=['steelblue','teal','coral'])
plt.title('Sales by Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('chart_category_sales.png')
plt.show()

# ── Chart 3: Top 10 Sub-Categories ────────────────
sub_sales = df.groupby('sub-category')['sales'].sum().sort_values(ascending=True).tail(10)

plt.figure(figsize=(8,5))
sub_sales.plot(kind='barh', color='steelblue')
plt.title('Top 10 Sub-Categories by Sales')
plt.xlabel('Sales ($)')
plt.tight_layout()
plt.savefig('chart_subcategory.png')
plt.show()

# ── Chart 4: Regional Performance ──────────────────
region = df.groupby('region')[['sales','profit']].sum().reset_index()

fig, ax = plt.subplots(figsize=(8,4))
x = range(len(region))
ax.bar([i-0.2 for i in x], region['sales'], width=0.4, label='Sales', color='steelblue')
ax.bar([i+0.2 for i in x], region['profit'], width=0.4, label='Profit', color='coral')
ax.set_xticks(x)
ax.set_xticklabels(region['region'])
ax.set_title('Sales vs Profit by Region')
ax.legend()
plt.tight_layout()
plt.savefig('chart_region.png')
plt.show()

# ── Chart 5: Profit Margin Distribution ───────────
plt.figure(figsize=(8,4))
sns.histplot(df['profit_margin'], bins=40, color='steelblue', kde=True)
plt.title('Profit Margin Distribution')
plt.xlabel('Profit Margin (%)')
plt.tight_layout()
plt.savefig('chart_profit_margin.png')
plt.show()

print("All charts saved!")