import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Đọc dữ liệu ---
try:
    # Đọc file CSV
    df = pd.read_csv('insurance.csv')
    print("✅ Đã đọc dữ liệu thành công!")
    print(f"Tổng số dòng: {len(df)}")
except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy file 'insurance.csv'.")
    print("Hãy chắc chắn file csv nằm cùng thư mục với file code này.")
    exit()

# --- 2. Phân tích Khu vực (Region) ---
print("\n--- PHÂN TÍCH KHU VỰC ---")
region_counts = df['region'].value_counts()
print("Số lượng người theo khu vực:")
print(region_counts)

# Tìm khu vực cao nhất
top_region = region_counts.idxmax()
print(f"-> Khu vực có nhiều người tham gia nhất: {top_region} ({region_counts.max()} người)")

# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 6))
plt.pie(region_counts, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Tỷ lệ người tham gia bảo hiểm theo khu vực')
print("-> Đang hiển thị biểu đồ tròn...")
plt.show()

# --- 3. Tính xác suất ---
print("\n--- PHÂN TÍCH XÁC SUẤT ---")

# Xác suất P(Smoker)
p_smoker = (df['smoker'] == 'yes').mean()
print(f"Xác suất là người hút thuốc P(Smoker): {p_smoker:.2%}")

# Xác suất P(Charges > 15000)
p_high_charges = (df['charges'] > 15000).mean()
print(f"Xác suất chi phí > 15,000 USD: {p_high_charges:.2%}")