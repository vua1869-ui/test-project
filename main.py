import json
import os

FILE_NAME = "products.json"

# ------------------ XỬ LÝ FILE ------------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ------------------ CHỨC NĂNG ------------------
def show_products(data):
    if not data:
        print("\n⚠️ Danh sách trống!")
        return
    print("\n📦 DANH SÁCH SẢN PHẨM")
    print("-" * 40)
    for i, p in enumerate(data, 1):
        print(f"{i}. {p['name']} | Giá: {p['price']} | SL: {p['quantity']}")
    print("-" * 40)

def add_product(data):
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá: "))
    quantity = int(input("Nhập số lượng: "))

    data.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

    save_data(data)
    print("✅ Thêm sản phẩm thành công!")

def delete_product(data):
    show_products(data)
    if not data:
        return
    index = int(input("Nhập số thứ tự sản phẩm cần xóa: ")) - 1

    if 0 <= index < len(data):
        removed = data.pop(index)
        save_data(data)
        print(f"🗑️ Đã xóa: {removed['name']}")
    else:
        print("❌ Vị trí không hợp lệ")

def update_product(data):
    show_products(data)
    if not data:
        return
    index = int(input("Nhập số thứ tự sản phẩm cần sửa: ")) - 1

    if 0 <= index < len(data):
        p = data[index]
        print("Nhấn Enter để giữ nguyên")

        name = input(f"Tên ({p['name']}): ") or p["name"]
        price_input = input(f"Giá ({p['price']}): ")
        quantity_input = input(f"Số lượng ({p['quantity']}): ")

        p["name"] = name
        p["price"] = float(price_input) if price_input else p["price"]
        p["quantity"] = int(quantity_input) if quantity_input else p["quantity"]

        save_data(data)
        print("✏️ Cập nhật thành công!")
    else:
        print("❌ Vị trí không hợp lệ")

# ------------------ MENU ------------------
def menu():
    data = load_data()

    while True:
        print("\n====== QUẢN LÝ SẢN PHẨM ======")
        print("1. Xem danh sách")
        print("2. Thêm sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Sửa sản phẩm")
        print("0. Thoát")
        print("=============================")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            show_products(data)
        elif choice == "2":
            add_product(data)
        elif choice == "3":
            delete_product(data)
        elif choice == "4":
            update_product(data)
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# ------------------ CHẠY ------------------
if __name__ == "__main__":
    menu()
