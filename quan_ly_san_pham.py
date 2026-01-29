import json
import os

# Tên file để lưu dữ liệu
DATA_FILE = "products.json"

# Biến toàn cục để lưu danh sách sản phẩm trong bộ nhớ khi chương trình chạy
products = []

def load_data():
    """
    Đọc dữ liệu từ file JSON và gán vào biến products.
    Nếu file không tồn tại, trả về danh sách rỗng.
    """
    global products
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                products = json.load(f)
            print(f"--> Đã tải {len(products)} sản phẩm từ kho dữ liệu.")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            products = []
    else:
        products = []
        print("--> Chưa có dữ liệu cũ. Khởi tạo kho hàng mới.")

def save_data():
    """
    Ghi danh sách products hiện tại vào file JSON.
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=4, ensure_ascii=False)
        print("--> Đã lưu dữ liệu thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def get_all_products():
    """Trả về danh sách tất cả sản phẩm"""
    return products

# Bạn có thể thêm các hàm logic khác ở đây (Thêm, Sửa, Xóa...) trong các phần sau