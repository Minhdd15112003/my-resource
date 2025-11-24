"""
Bài 4: List trong Python
- Khởi tạo và truy cập list
- Các phương thức của list
- List slicing
- List comprehension
- Các bài toán thường gặp với list
"""

# 1. KHỞI TẠO LIST
# Cách 1: Khởi tạo trực tiếp
numbers = [1, 2, 3, 4, 5]
fruits = ["táo", "cam", "chuối"]
mixed = [1, "hello", 3.14, True]  # List có thể chứa nhiều kiểu dữ liệu

# Cách 2: Tạo list rỗng
empty_list = []
empty_list2 = list()

# Cách 3: Tạo list với giá trị lặp lại
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# 2. TRUY CẬP PHẦN TỬ
print(f"Phần tử đầu tiên: {numbers[0]}")
print(f"Phần tử cuối cùng: {numbers[-1]}")
print(f"Phần tử thứ 3: {numbers[2]}")

# 3. CÁC PHƯƠNG THỨC CỦA LIST
my_list = [1, 2, 3]

# Thêm phần tử
my_list.append(4)  # Thêm vào cuối: [1, 2, 3, 4]
my_list.insert(1, 10)  # Chèn vào vị trí 1: [1, 10, 2, 3, 4]
my_list.extend([5, 6])  # Thêm nhiều phần tử: [1, 10, 2, 3, 4, 5, 6]

# Xóa phần tử
my_list.pop()  # Xóa phần tử cuối
my_list.pop(1)  # Xóa phần tử tại vị trí 1
my_list.remove(3)  # Xóa giá trị 3 đầu tiên tìm thấy

# Các phương thức khác
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # Sắp xếp tăng dần
print(f"Sắp xếp tăng: {numbers}")

numbers.sort(reverse=True)  # Sắp xếp giảm dần
print(f"Sắp xếp giảm: {numbers}")

numbers.reverse()  # Đảo ngược list
print(f"Đảo ngược: {numbers}")

# 4. LIST SLICING
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cú pháp: list[start:stop:step]
print(f"3 phần tử đầu: {arr[:3]}")  # [0, 1, 2]
print(f"3 phần tử cuối: {arr[-3:]}")  # [7, 8, 9]
print(f"Từ vị trí 2 đến 5: {arr[2:6]}")  # [2, 3, 4, 5]
print(f"Lấy số chẵn: {arr[::2]}")  # [0, 2, 4, 6, 8]
print(f"Đảo ngược: {arr[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 5. LIST COMPREHENSION
# Cú pháp: [biểu_thức for biến in iterable if điều_kiện]

# Tạo list bình phương
squares = [x**2 for x in range(10)]
print(f"Bình phương: {squares}")

# Lọc số chẵn
evens = [x for x in range(20) if x % 2 == 0]
print(f"Số chẵn: {evens}")

# List comprehension phức tạp
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Ma trận: {matrix}")

# 6. CÁC BÀI TOÁN THƯỜNG GẶP

# Bài toán 1: Tìm min, max
def tim_min_max(lst):
    """Tìm giá trị nhỏ nhất và lớn nhất"""
    if not lst:
        return None, None
    return min(lst), max(lst)

numbers = [5, 2, 8, 1, 9, 3]
min_val, max_val = tim_min_max(numbers)
print(f"Min: {min_val}, Max: {max_val}")

# Bài toán 2: Đếm số lần xuất hiện
def dem_so_lan(lst):
    """Đếm số lần xuất hiện của mỗi phần tử"""
    count = {}
    for x in lst:
        count[x] = count.get(x, 0) + 1
    return count

arr = [1, 2, 3, 1, 2, 1, 4, 5, 4]
print(f"Số lần xuất hiện: {dem_so_lan(arr)}")

# Bài toán 3: Mảng đánh dấu
def mang_danh_dau(lst):
    """Sử dụng mảng đánh dấu để đếm"""
    if not lst:
        return

    max_val = max(lst)
    count = [0] * (max_val + 1)

    for x in lst:
        count[x] += 1

    for i in range(len(count)):
        if count[i] > 0:
            print(f"Số {i} xuất hiện {count[i]} lần")

arr = [1, 2, 3, 1, 3, 2, 5, 7, 5]
mang_danh_dau(arr)

# 7. FILTER VÀ MAP
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter: lọc phần tử thỏa điều kiện
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter số chẵn: {evens}")

# Map: áp dụng hàm lên từng phần tử
squares = list(map(lambda x: x**2, numbers))
print(f"Map bình phương: {squares}")

# 8. UNPACKING LIST
coords = [10, 20, 30]
x, y, z = coords  # Unpacking
print(f"x={x}, y={y}, z={z}")

# Unpacking với *
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")
