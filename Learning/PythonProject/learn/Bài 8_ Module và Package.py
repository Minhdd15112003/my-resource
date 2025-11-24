"""
Bài 8: Module và Package trong Python
- Import module
- Tạo module riêng
- Package
- Module phổ biến
"""

# 1. IMPORT MODULE
print("=== IMPORT MODULE ===")

# Import toàn bộ module
import math
print(f"Pi = {math.pi}")
print(f"Căn 16 = {math.sqrt(16)}")

# Import cụ thể
from datetime import datetime, date
print(f"Ngày giờ hiện tại: {datetime.now()}")
print(f"Ngày hôm nay: {date.today()}")

# Import với alias (bí danh)
import numpy as np  # Nếu đã cài numpy
import pandas as pd  # Nếu đã cài pandas

# Import tất cả (không khuyến khích)
from random import *
print(f"Số ngẫu nhiên: {randint(1, 100)}")

# 2. TẠO MODULE RIÊNG
# File: my_math.py
"""
# my_math.py - Module toán học tự tạo

def cong(a, b):
    '''Phép cộng'''
    return a + b

def tru(a, b):
    '''Phép trừ'''
    return a - b

def nhan(a, b):
    '''Phép nhân'''
    return a * b

def chia(a, b):
    '''Phép chia'''
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b

def giai_thua(n):
    '''Tính giai thừa'''
    if n < 0:
        raise ValueError("n phải >= 0")
    if n <= 1:
        return 1
    return n * giai_thua(n - 1)

# Biến module
PI = 3.14159
E = 2.71828
"""

# 3. SỬ DỤNG MODULE TỰ TẠO
# import my_math
# print(my_math.cong(5, 3))
# print(my_math.PI)

# 4. CÁC MODULE QUAN TRỌNG
print("\n=== MODULE QUAN TRỌNG ===")

# A. Module math
import math
print("--- Module math ---")
print(f"Căn bậc 2: {math.sqrt(25)}")
print(f"Lũy thừa: {math.pow(2, 3)}")
print(f"Làm tròn lên: {math.ceil(4.3)}")
print(f"Làm tròn xuống: {math.floor(4.7)}")
print(f"Giai thừa: {math.factorial(5)}")
print(f"USCLN: {math.gcd(48, 18)}")

# B. Module random
import random
print("\n--- Module random ---")
print(f"Số ngẫu nhiên 0-1: {random.random()}")
print(f"Số nguyên ngẫu nhiên: {random.randint(1, 10)}")

lst = [1, 2, 3, 4, 5]
print(f"Chọn ngẫu nhiên: {random.choice(lst)}")
random.shuffle(lst)
print(f"Xáo trộn: {lst}")

# C. Module datetime
from datetime import datetime, timedelta
print("\n--- Module datetime ---")

now = datetime.now()
print(f"Thời gian hiện tại: {now}")
print(f"Năm: {now.year}, Tháng: {now.month}, Ngày: {now.day}")
print(f"Giờ: {now.hour}, Phút: {now.minute}, Giây: {now.second}")

# Tính toán với thời gian
tomorrow = now + timedelta(days=1)
print(f"Ngày mai: {tomorrow.date()}")

# Format thời gian
print(f"Format: {now.strftime('%d/%m/%Y %H:%M:%S')}")

# D. Module os
import os
print("\n--- Module os ---")
print(f"Thư mục hiện tại: {os.getcwd()}")
print(f"Danh sách file: {os.listdir('.')[:5]}...")  # 5 file đầu
print(f"Biến môi trường PATH: {os.environ.get('PATH', 'Không có')[:50]}...")

# E. Module sys
import sys
print("\n--- Module sys ---")
print(f"Phiên bản Python: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Đường dẫn Python: {sys.path[0]}")

# 5. PACKAGE
print("\n=== PACKAGE ===")

# Cấu trúc package:
"""
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        module3.py
"""

# Import từ package
# from my_package import module1
# from my_package.sub_package import module3

# 6. VÍ DỤ THỰC TẾ: MODULE TIỆN ÍCH
# File: utils.py
"""
# utils.py - Module tiện ích

import re
import json
from datetime import datetime

def validate_email(email):
    '''Kiểm tra email hợp lệ'''
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    '''Kiểm tra số điện thoại VN'''
    pattern = r'^(0|\+84)[0-9]{9,10}$'
    return re.match(pattern, phone) is not None

def read_json_file(filename):
    '''Đọc file JSON'''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Lỗi đọc file: {e}")
        return None

def write_json_file(filename, data):
    '''Ghi file JSON'''
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Lỗi ghi file: {e}")
        return False

def format_currency(amount):
    '''Format số thành tiền VND'''
    return f"{amount:,.0f}đ".replace(',', '.')

def time_ago(dt):
    '''Tính thời gian đã qua'''
    now = datetime.now()
    diff = now - dt
    
    if diff.days > 365:
        return f"{diff.days // 365} năm trước"
    elif diff.days > 30:
        return f"{diff.days // 30} tháng trước"
    elif diff.days > 0:
        return f"{diff.days} ngày trước"
    elif diff.seconds > 3600:
        return f"{diff.seconds // 3600} giờ trước"
    elif diff.seconds > 60:
        return f"{diff.seconds // 60} phút trước"
    else:
        return "Vừa xong"

class Timer:
    '''Context manager để đo thời gian'''
    def __enter__(self):
        self.start = datetime.now()
        return self
    
    def __exit__(self, *args):
        self.end = datetime.now()
        self.duration = self.end - self.start
        print(f"Thời gian thực thi: {self.duration.total_seconds():.3f} giây")
"""

# Sử dụng module utils
# import utils
#
# with utils.Timer():
#     # Code cần đo thời gian
#     time.sleep(1)

# 7. QUẢN LÝ DEPENDENCIES
print("\n=== QUẢN LÝ DEPENDENCIES ===")

# requirements.txt
"""
numpy==1.21.0
pandas==1.3.0
requests==2.26.0
matplotlib==3.4.2
"""

# Cài đặt: pip install -r requirements.txt
# Xuất: pip freeze > requirements.txt

# 8. BEST PRACTICES
print("\n=== BEST PRACTICES ===")

# 1. Đặt tên module: lowercase_with_underscore
# 2. Docstring cho module
# 3. Tránh import *
# 4. Tổ chức import theo thứ tự:
#    - Standard library
#    - Third-party
#    - Local modules
# 5. Sử dụng if __name__ == "__main__":

if __name__ == "__main__":
    print("Module này đang chạy trực tiếp")
