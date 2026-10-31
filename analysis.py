import pandas as pd

# 1. قراءة ملف البيانات
df = pd.read_csv('agricultural_data.csv')

# 2. عرض ملخص البيانات
print("--- معاينة البيانات ---")
print(df.head())

# 3. حساب المتوسطات الحسابية
avg_temp = df['Temperature (°C)'].mean()
avg_soil_moisture = df['Soil_Moisture (%)'].mean()
total_water_used = df['Irrigation_Water_Liters'].sum()

print("\n--- نتائج التحليل الأساسية ---")
print(f"متوسط درجة الحرارة: {avg_temp:.1f} °C")
print(f"متوسط رطوبة التربة: {avg_soil_moisture:.1f} %")
print(f"إجمالي مياه الري المستخدمة: {total_water_used} لتر")

# 4. تحديد الأيام التي كانت فيها التربة جافة وحتاجة للري
dry_days = df[df['Soil_Moisture (%)'] < 30]
print("\n--- الأيام التي انخفضت فيها رطوبة التربة عن 30% ---")
print(dry_days[['Date', 'Temperature (°C)', 'Soil_Moisture (%)']])
