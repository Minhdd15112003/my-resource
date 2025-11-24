"""
Bài 5: Tuple, Set và Dictionary
- Tuple: immutable list
- Set: tập hợp không trùng lặp
- Dictionary: cấu trúc key-value
"""

# 1. TUPLE - DANH SÁCH KHÔNG THAY ĐỔI
print("=== TUPLE ===")

# Khởi tạo tuple
empty_tuple = ()
single_tuple = (1,)  # Chú ý dấu phẩy
coordinates = (10, 20, 30)
mixed = (1, "hello", 3.14)

# Truy cập phần tử (giống list)
print(f"Tọa độ x: {coordinates[0]}")
print(f"Tọa độ y: {coordinates[1]}")

# Unpacking tuple
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Tuple là immutable (không thể thay đổi)
# coordinates[0] = 100  # Lỗi!

# Sử dụng tuple
def get_min_max(lst):
    """Trả về tuple (min, max)"""
    return min(lst), max(lst)

numbers = [5, 2, 8, 1, 9]
min_val, max_val = get_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

# 2. SET - TẬP HỢP
print("\n=== SET ===")

# Khởi tạo set
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 4])  # Loại bỏ trùng lặp
print(f"Set từ list: {from_list}")

# Thêm/xóa phần tử
my_set = {1, 2, 3}
my_set.add(4)  # Thêm phần tử
my_set.remove(2)  # Xóa phần tử (lỗi nếu không tồn tại)
my_set.discard(10)  # Xóa phần tử (không lỗi)
print(f"Set sau khi thay đổi: {my_set}")

# Các phép toán tập hợp
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Hợp: {set1 | set2}")  # {1, 2, 3, 4, 5, 6}
print(f"Giao: {set1 & set2}")  # {3, 4}
print(f"Hiệu: {set1 - set2}")  # {1, 2}
print(f"Hiệu đối xứng: {set1 ^ set2}")  # {1, 2, 5, 6}

# Ứng dụng: Loại bỏ trùng lặp
lst = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = list(set(lst))
print(f"Danh sách unique: {unique}")

# 3. DICTIONARY - TỪ ĐIỂN
print("\n=== DICTIONARY ===")

# Khởi tạo dictionary
empty_dict = {}
person = {
    "name": "An",
    "age": 20,
    "city": "Hà Nội"
}

# Truy cập phần tử
print(f"Tên: {person['name']}")
print(f"Tuổi: {person.get('age')}")
print(f"Quốc gia: {person.get('country', 'Việt Nam')}")  # Giá trị mặc định

# Thêm/sửa phần tử
person['email'] = 'an@gmail.com'  # Thêm
person['age'] = 21  # Sửa
print(f"Sau khi cập nhật: {person}")

# Xóa phần tử
del person['city']  # Xóa bằng del
email = person.pop('email')  # Xóa và lấy giá trị
print(f"Email đã xóa: {email}")

# Duyệt dictionary
student = {
    "name": "Bình",
    "scores": {"math": 9, "physics": 8, "chemistry": 7}
}

# Duyệt keys
for key in student:
    print(f"Key: {key}")

# Duyệt key-value
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"Bình phương: {squares}")

# 4. ỨNG DỤNG KẾT HỢP
print("\n=== ỨNG DỤNG ===")

# Đếm tần suất xuất hiện
def dem_tan_suat(lst):
    """Đếm tần suất dùng dictionary"""
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(f"Tần suất: {dem_tan_suat(words)}")

# Nhóm dữ liệu
def nhom_theo_do_dai(words):
    """Nhóm từ theo độ dài"""
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

words = ["a", "bb", "ccc", "dd", "e", "fff"]
print(f"Nhóm theo độ dài: {nhom_theo_do_dai(words)}")

# Set để kiểm tra membership nhanh
valid_users = {"admin", "user1", "user2", "guest"}
username = "admin"
if username in valid_users:
    print(f"{username} hợp lệ")

# Nested structures
school = {
    "classes": {
        "10A": ["An", "Bình", "Cường"],
        "10B": ["Dũng", "Em", "Phương"]
    },
    "teachers": {
        "math": "Thầy A",
        "physics": "Cô B"
    }
}

print(f"Học sinh lớp 10A: {school['classes']['10A']}")
print(f"Giáo viên Toán: {school['teachers']['math']}")
