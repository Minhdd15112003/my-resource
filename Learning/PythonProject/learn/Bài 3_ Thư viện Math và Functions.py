"""
Bài 3: Hàm trong Python
- Định nghĩa và gọi hàm
- Tham số và giá trị trả về
- Phạm vi biến (scope)
- Lambda function
- Hàm đệ quy
"""

import math

# 1. ĐỊNH NGHĨA HÀM CƠ BẢN
def chao_mung():
    """Hàm đơn giản không tham số"""
    print("Chào mừng đến với Python!")

# Gọi hàm
chao_mung()

# 2. HÀM CÓ THAM SỐ
def tinh_tong(a, b):
    """Hàm tính tổng 2 số"""
    return a + b

# Gọi hàm
ketqua = tinh_tong(5, 3)
print(f"5 + 3 = {ketqua}")

# 3. HÀM VỚI THAM SỐ MẶC ĐỊNH
def gioi_thieu(ten, tuoi=18):
    """Hàm với tham số mặc định"""
    print(f"Tên: {ten}, Tuổi: {tuoi}")

gioi_thieu("An")  # tuoi = 18 (mặc định)
gioi_thieu("Bình", 25)

# 4. HÀM VỚI SỐ THAM SỐ KHÔNG XÁC ĐỊNH
# *args: nhận nhiều tham số vị trí
def tinh_tong_nhieu_so(*args):
    """Tính tổng nhiều số"""
    return sum(args)

print(tinh_tong_nhieu_so(1, 2, 3, 4, 5))

# **kwargs: nhận nhiều tham số từ khóa
def thong_tin(**kwargs):
    """In thông tin dạng key-value"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

thong_tin(ten="An", tuoi=20, lop="12A1")

# 5. HÀM KIỂM TRA SỐ NGUYÊN TỐ
def kiem_tra_nguyen_to(n):
    """
    Kiểm tra số nguyên tố
    Args:
        n: số cần kiểm tra
    Returns:
        True nếu là số nguyên tố, False nếu không
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test hàm
for i in range(20):
    if kiem_tra_nguyen_to(i):
        print(i, end=" ")
print()

# 6. LAMBDA FUNCTION
# Lambda là hàm ẩn danh, viết gọn trên 1 dòng
binh_phuong = lambda x: x ** 2
print(f"5^2 = {binh_phuong(5)}")

# Lambda với nhiều tham số
tong = lambda x, y, z: x + y + z
print(f"Tổng = {tong(1, 2, 3)}")

# 7. HÀM ĐỆ QUY
def giai_thua(n):
    """Tính giai thừa bằng đệ quy"""
    if n <= 1:
        return 1
    return n * giai_thua(n - 1)

print(f"5! = {giai_thua(5)}")

# 8. PHẠM VI BIẾN (SCOPE)
bien_global = "Tôi là biến global"

def ham_scope():
    bien_local = "Tôi là biến local"
    print(bien_global)  # Có thể truy cập biến global
    print(bien_local)

    # Thay đổi biến global
    global bien_global
    bien_global = "Đã thay đổi"

ham_scope()
print(bien_global)  # Đã bị thay đổi

# 9. HÀM TRẢ VỀ NHIỀU GIÁ TRỊ
def tinh_toan(a, b):
    """Trả về nhiều kết quả"""
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b if b != 0 else None
