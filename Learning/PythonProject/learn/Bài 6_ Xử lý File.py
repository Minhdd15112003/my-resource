"""
Bài 6: Xử lý File trong Python
- Đọc/ghi file text
- Xử lý file JSON
- Quản lý đường dẫn
- Xử lý lỗi file
"""

import os
import json
from pathlib import Path

# 1. ĐỌC FILE TEXT
print("=== ĐỌC FILE ===")

# Cách 1: Đọc toàn bộ file
try:
    with open('data.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("Nội dung file:")
        print(content)
except FileNotFoundError:
    print("File không tồn tại!")

# Cách 2: Đọc từng dòng
def doc_tung_dong(filename):
    """Đọc và xử lý từng dòng"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                print(f"Dòng {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}")

# Cách 3: Đọc vào list
def doc_vao_list(filename):
    """Đọc tất cả dòng vào list"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Loại bỏ ký tự xuống dòng
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        return []

# 2. GHI FILE TEXT
print("\n=== GHI FILE ===")

# Ghi đè file
def ghi_file(filename, content):
    """Ghi nội dung vào file (ghi đè)"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Đã ghi file {filename}")

# Ghi thêm vào file
def ghi_them(filename, content):
    """Ghi thêm nội dung vào cuối file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')
    print(f"Đã ghi thêm vào {filename}")

# Ghi list vào file
def ghi_list(filename, lst):
    """Ghi mỗi phần tử của list thành một dòng"""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in lst:
            file.write(str(item) + '\n')

# Test ghi file
students = ["An", "Bình", "Cường", "Dũng"]
ghi_list('students.txt', students)

# 3. XỬ LÝ FILE JSON
print("\n=== FILE JSON ===")

# Đọc JSON
def doc_json(filename):
    """Đọc dữ liệu từ file JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {filename} không tồn tại")
        return None
    except json.JSONDecodeError:
        print(f"File {filename} không phải JSON hợp lệ")
        return None

# Ghi JSON
def ghi_json(filename, data):
    """Ghi dữ liệu vào file JSON"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Đã ghi dữ liệu vào {filename}")

# Ví dụ sử dụng JSON
student_data = {
    "students": [
        {"name": "An", "age": 20, "grades": [8, 9, 7]},
        {"name": "Bình", "age": 21, "grades": [9, 8, 9]},
        {"name": "Cường", "age": 19, "grades": [7, 8, 8]}
    ],
    "class": "10A",
    "year": 2024
}

# Ghi và đọc lại JSON
ghi_json('students.json', student_data)
loaded_data = doc_json('students.json')
if loaded_data:
    print(f"Lớp: {loaded_data['class']}")
    print(f"Số học sinh: {len(loaded_data['students'])}")

# 4. QUẢN LÝ ĐƯỜNG DẪN VÀ THƯ MỤC
print("\n=== QUẢN LÝ ĐƯỜNG DẪN ===")

# Sử dụng os module
current_dir = os.getcwd()
print(f"Thư mục hiện tại: {current_dir}")

# Kiểm tra file/thư mục tồn tại
if os.path.exists('data.txt'):
    print("File data.txt tồn tại")
    print(f"Kích thước: {os.path.getsize('data.txt')} bytes")

# Tạo thư mục
def tao_thu_muc(path):
    """Tạo thư mục nếu chưa tồn tại"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Đã tạo thư mục: {path}")
    else:
        print(f"Thư mục {path} đã tồn tại")

# Liệt kê files trong thư mục
def liet_ke_files(directory='.'):
    """Liệt kê tất cả files trong thư mục"""
    files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item)
    return files

# Sử dụng pathlib (cách hiện đại hơn)
def pathlib_example():
    """Ví dụ sử dụng pathlib"""
    # Tạo Path object
    current = Path.cwd()
    print(f"Thư mục hiện tại: {current}")

    # Tạo đường dẫn
    data_dir = current / 'data'
    data_file = data_dir / 'output.txt'

    # Tạo thư mục
    data_dir.mkdir(exist_ok=True)

    # Ghi file
    data_file.write_text("Hello from pathlib!", encoding='utf-8')

    # Đọc file
    if data_file.exists():
        content = data_file.read_text(encoding='utf-8')
        print(f"Nội dung: {content}")

    # Lấy thông tin file
    print(f"Tên file: {data_file.name}")
    print(f"Phần mở rộng: {data_file.suffix}")
    print(f"Thư mục cha: {data_file.parent}")

# 5. XỬ LÝ LỖI KHI LÀM VIỆC VỚI FILE
print("\n=== XỬ LÝ LỖI ===")

def doc_file_an_toan(filename):
    """Đọc file với xử lý lỗi đầy đủ"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Lỗi: File '{filename}' không tồn tại")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{filename}'")
    except UnicodeDecodeError:
        print(f"Lỗi: File '{filename}' không phải UTF-8")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    return None

# 6. VÍ DỤ THỰC TẾ: QUẢN LÝ ĐIỂM HỌC SINH
class QuanLyDiem:
    """Class quản lý điểm học sinh với file"""

    def __init__(self, filename='diem.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Tải dữ liệu từ file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"students": {}}

    def save_data(self):
        """Lưu dữ liệu vào file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def them_diem(self, ten, mon, diem):
        """Thêm điểm cho học sinh"""
        if ten not in self.data["students"]:
            self.data["students"][ten] = {}
        self.data["students"][ten][mon] = diem
        self.save_data()
        print(f"Đã thêm điểm {mon}: {diem} cho {ten}")

    def xem_diem(self, ten):
        """Xem điểm của học sinh"""
        if ten in self.data["students"]:
            print(f"\nĐiểm của {ten}:")
            for mon, diem in self.data["students"][ten].items():
                print(f"  {mon}: {diem}")
        else:
            print(f"Không tìm thấy học sinh {ten}")

    def tinh_trung_binh(self, ten):
        """Tính điểm trung bình"""
        if ten in self.data["students"]:
            diem_list = list(self.data["students"][ten].values())
            if diem_list:
                tb = sum(diem_list) / len(diem_list)
                print(f"Điểm trung bình của {ten}: {tb:.2f}")
                return tb
        return 0

# Sử dụng class
if __name__ == "__main__":
    # Test các hàm
    print("=== TEST CÁC CHỨC NĂNG ===")

    # Test ghi/đọc file text
    ghi_file('test.txt', 'Hello Python!\nXin chào!')
    content = doc_file_an_toan('test.txt')
    if content:
        print(f"Đã đọc: {content}")

    # Test quản lý điểm
    ql = QuanLyDiem()
    ql.them_diem("An", "Toán", 8.5)
    ql.them_diem("An", "Lý", 9.0)
    ql.them_diem("An", "Hóa", 7.5)
    ql.xem_diem("An")
    ql.tinh_trung_binh("An")
