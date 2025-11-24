"""
Bài 1: Kiểu dữ liệu cơ bản trong Python
- Biến và cách khai báo
- Các kiểu dữ liệu: int, float, string, boolean
- Ép kiểu dữ liệu
- Nhập xuất cơ bản
"""

# 1. KHAI BÁO BIẾN VÀ KIỂU DỮ LIỆU
# Python tự động nhận diện kiểu dữ liệu
chuoi = "Hello Python"  # String (chuỗi)
so_nguyen = 123456     # Integer (số nguyên)
so_thuc = 3.14159      # Float (số thực)
boolean = True         # Boolean (True/False)

# 2. KIỂM TRA KIỂU DỮ LIỆU
print(f"Kiểu của chuoi: {type(chuoi)}")
print(f"Kiểu của so_nguyen: {type(so_nguyen)}")
print(f"Kiểu của so_thuc: {type(so_thuc)}")
print(f"Kiểu của boolean: {type(boolean)}")

# 3. ÉP KIỂU DỮ LIỆU
# String sang số
num_str = "123"
num = int(num_str)  # Chuyển string sang int
print(f"{num_str} -> {num}")

# Float sang int (làm tròn xuống)
pi = 3.14159
pi_int = int(pi)
print(f"{pi} -> {pi_int}")

# Số sang string
age = 25
age_str = str(age)
print(f"Tôi {age_str} tuổi")

# 4. ĐỊNH DẠNG SỐ THỰC
so_thuc = 2.2679890
print(f"Số gốc: {so_thuc}")
print(f"Làm tròn 2 chữ số: {so_thuc:.2f}")
print(f"Làm tròn 4 chữ số: {so_thuc:.4f}")
print("Cách cũ: %.4f" % so_thuc)

# 5. NHẬP DỮ LIỆU TỪ BÀN PHÍM
# Nhập một giá trị
name = input("Nhập tên của bạn: ")
print(f"Xin chào, {name}!")

# Nhập số nguyên
age = int(input("Nhập tuổi: "))
print(f"Năm sau bạn {age + 1} tuổi")

# Nhập nhiều giá trị trên một dòng
print("Nhập 3 số cách nhau bởi dấu cách:")
x, y, z = map(int, input().split())
print(f"Tổng: {x + y + z}")

# 6. KHAI BÁO NHIỀU BIẾN
a, b, c = 1, 2, 3  # Gán nhiều giá trị cùng lúc
x = y = z = 0      # Gán cùng một giá trị

# 7. HẰNG SỐ (quy ước dùng chữ in hoa)
PI = 3.14159
GRAVITY = 9.8

# 8. KIỂU NONE
result = None  # Giá trị rỗng
print(f"result = {result}, type = {type(result)}")
