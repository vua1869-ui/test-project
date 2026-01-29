import product_manager

def san_pham():
    # 1. Tải dữ liệu khi chương trình bắt đầu
    ds_san_pham = product_manager.load_products()
    
    while True:
        print("=== QUẢN LÝ CỬA HÀNG LAPTOP POLYLAP ===")
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Sửa thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Thoát & Lưu dữ liệu")
        
        san_pham = input("Mời bạn chọn chức năng (1-5): ")
        
        if san_pham == '1':
            print("\n--- Danh sách sản phẩm ---")
            # Sẽ gọi hàm hiển thị từ product_manager sau
            print(ds_san_pham) 
        elif san_pham == '2':
            pass # Sẽ xử lý sau
        elif san_pham == '0':
            product_manager.save_products(ds_san_pham)
            print("Tạm biệt! nhớ ghé tôi nhá .")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    san_pham()