"""
Bài 2: Câu lệnh điều khiển trong Python
- Câu lệnh if-elif-else
- Toán tử điều kiện
- Vòng lặp for và while
- break, continue, pass
"""

# 1. CÂU LỆNH IF-ELIF-ELSE
age = int(input("Nhập tuổi: "))

if age < 18:
    print("Bạn là trẻ em")
elif age < 60:
    print("Bạn là người trưởng thành")
else:
    print("Bạn là người cao tuổi")

# 2. TOÁN TỬ ĐIỀU KIỆN (Ternary operator)
score = int(input("Nhập điểm: "))
result = "Đậu" if score >= 5 else "Rớt"
print(result)

# 3. TOÁN TỬ SO SÁNH VÀ LOGIC
# So sánh: ==, !=, <, >, <=, >=
# Logic: and, or, not
x = 10
if x > 0 and x < 100:
    print("x nằm trong khoảng (0, 100)")

# 4. VÒNG LẶP FOR
print("\n--- Vòng lặp FOR ---")

# For với range
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i, end=" ")
print()

# Lặp ngược
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 5. VÒNG LẶP WHILE
print("\n--- Vòng lặp WHILE ---")
count = 0
while count < 5:
    print(f"Count = {count}")
    count += 1

# 6. BREAK VÀ CONTINUE
print("\n--- Break và Continue ---")
# Break: thoát khỏi vòng lặp
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# Continue: bỏ qua lần lặp hiện tại
for i in range(10):
    if i % 2 == 0:
        continue  # Bỏ qua số chẵn
    print(i, end=" ")
print()

# 7. VÒNG LẶP LỒNG NHAU
print("\n--- Vòng lặp lồng nhau ---")
# In bảng cửu chương
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()  # Xuống dòng

# 8. ELSE TRONG VÒNG LẶP
# else sẽ chạy khi vòng lặp kết thúc bình thường (không break)
for i in range(5):
    if i == 10:  # Điều kiện không bao giờ đúng
        break
else:
    print("Vòng lặp kết thúc bình thường")

# 9. PASS STATEMENT
# Dùng khi cần một câu lệnh rỗng
x = 10
if x > 0:
    pass  # Sẽ xử lý sau
else:
    print("x <= 0")
