import statistics
import csv

# Leer datos mensuales de ventas desde un CSV
monthly_sales = {}
with open('monthly-sales.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())

# Cálculo de estadísticas
mean_sales = round(statistics.mean(sales))
median_sales = round(statistics.median(sales))
mode_sales = round(statistics.mode(sales))
stdev_sales = round(statistics.stdev(sales))
variance_sales = round(statistics.variance(sales))
max_sales = max(sales)
min_sales = min(sales)
range_sales = max_sales - min_sales

# Formateo de salida
print("=" * 40)
print("📊 Resumen de Ventas Mensuales 📊")
print("=" * 40)
print(f"🔹 Media de ventas: {mean_sales:,} COP")
print(f"🔹 Mediana de ventas: {median_sales:,} COP")
print(f"🔹 Moda de ventas: {mode_sales:,} COP")
print(f"🔹 Desviación estándar: {stdev_sales:,} COP")
print(f"🔹 Varianza de ventas: {variance_sales:,} COP")
print(f"🔹 Máximo de ventas: {max_sales:,} COP")
print(f"🔹 Mínimo de ventas: {min_sales:,} COP")
print(f"🔹 Rango de ventas: {range_sales:,} COP")
print("=" * 40)
