import pandas as pd
import sqlite3

df = pd.read_csv('superstore_clean.csv')

# Load into SQLite (so you can run real SQL)
conn = sqlite3.connect('superstore.db')
df.to_sql('orders', conn, if_exists='replace', index=False)

# ── Query 1: Total KPIs ────────────────────────────
q1 = '''
SELECT
    ROUND(SUM(sales), 2)         AS total_sales,
    ROUND(SUM(profit), 2)        AS total_profit,
    COUNT(DISTINCT order_id)     AS total_orders,
    ROUND(AVG(profit_margin), 2) AS avg_profit_margin
FROM orders
'''
print("KPIs:\n", pd.read_sql(q1, conn))

# ── Query 2: Sales by Category ─────────────────────
q2 = '''
SELECT
    category,
    ROUND(SUM(sales), 2)  AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY category
ORDER BY total_sales DESC
'''
print("\nBy Category:\n", pd.read_sql(q2, conn))

# ── Query 3: Monthly Revenue Trend ────────────────
q3 = '''
SELECT
    order_year,
    order_month,
    order_month_name,
    ROUND(SUM(sales), 2) AS monthly_sales
FROM orders
GROUP BY order_year, order_month
ORDER BY order_year, order_month
'''
print("\nMonthly Trend:\n", pd.read_sql(q3, conn))

# ── Query 4: Top 5 Products by Sales ──────────────
q4 = '''
SELECT
    product_name,
    ROUND(SUM(sales), 2)  AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5
'''
print("\nTop 5 Products:\n", pd.read_sql(q4, conn))

# ── Query 5: Region Performance ───────────────────
q5 = '''
SELECT
    region,
    ROUND(SUM(sales), 2)         AS total_sales,
    ROUND(SUM(profit), 2)        AS total_profit,
    ROUND(AVG(profit_margin), 2) AS avg_margin
FROM orders
GROUP BY region
ORDER BY total_sales DESC
'''
print("\nBy Region:\n", pd.read_sql(q5, conn))

conn.close()
print("\nSQL analysis complete!")
