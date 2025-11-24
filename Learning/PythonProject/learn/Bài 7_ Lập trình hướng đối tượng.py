"""
Bài 7: Lập trình hướng đối tượng (OOP) trong Python
- Class và Object
- Thuộc tính và phương thức
- Kế thừa và đa hình
- Encapsulation
"""

# 1. CLASS VÀ OBJECT CƠ BẢN
print("=== CLASS VÀ OBJECT ===")

class SinhVien:
    """Class đại diện cho một sinh viên"""

    # Class attribute (thuộc tính chung cho tất cả object)
    truong = "Đại học ABC"

    # Constructor (hàm khởi tạo)
    def __init__(self, ho_ten, ma_sv, nam_sinh):
        # Instance attributes (thuộc tính riêng của mỗi object)
        self.ho_ten = ho_ten
        self.ma_sv = ma_sv
        self.nam_sinh = nam_sinh
        self.diem = {}  # Dictionary lưu điểm các môn

    # Instance method (phương thức)
    def them_diem(self, mon, diem):
        """Thêm điểm một môn học"""
        self.diem[mon] = diem

    def tinh_diem_tb(self):
        """Tính điểm trung bình"""
        if not self.diem:
            return 0
        return sum(self.diem.values()) / len(self.diem)

    def xep_loai(self):
        """Xếp loại học lực"""
        dtb = self.tinh_diem_tb()
        if dtb >= 8.5:
            return "Giỏi"
        elif dtb >= 7.0:
            return "Khá"
        elif dtb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        """Phương thức in object"""
        return f"SV: {self.ho_ten} - MSSV: {self.ma_sv}"

# Tạo và sử dụng object
sv1 = SinhVien("Nguyễn Văn An", "SV001", 2005)
sv1.them_diem("Toán", 8.5)
sv1.them_diem("Lý", 7.5)
sv1.them_diem("Hóa", 9.0)

print(sv1)  # Gọi __str__
print(f"Điểm TB: {sv1.tinh_diem_tb():.2f}")
print(f"Xếp loại: {sv1.xep_loai()}")
print(f"Trường: {SinhVien.truong}")

# 2. STATIC METHOD VÀ CLASS METHOD
print("\n=== STATIC & CLASS METHOD ===")

class TienIch:
    """Class chứa các phương thức tiện ích"""

    @staticmethod
    def kiem_tra_nam_nhuan(nam):
        """Static method: không cần self"""
        return nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)

    @classmethod
    def tao_ngay_hien_tai(cls):
        """Class method: nhận cls làm tham số đầu tiên"""
        from datetime import date
        today = date.today()
        return f"{today.day}/{today.month}/{today.year}"

# Sử dụng
print(f"2024 là năm nhuận: {TienIch.kiem_tra_nam_nhuan(2024)}")
print(f"Ngày hiện tại: {TienIch.tao_ngay_hien_tai()}")

# 3. KẾ THỪA (INHERITANCE)
print("\n=== KẾ THỪA ===")

class ConNguoi:
    """Lớp cha"""
    def __init__(self, ho_ten, nam_sinh):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh

    def tinh_tuoi(self):
        from datetime import date
        return date.today().year - self.nam_sinh

    def gioi_thieu(self):
        return f"Tôi là {self.ho_ten}, {self.tinh_tuoi()} tuổi"

class GiangVien(ConNguoi):
    """Lớp con kế thừa từ ConNguoi"""
    def __init__(self, ho_ten, nam_sinh, ma_gv, khoa):
        # Gọi constructor của lớp cha
        super().__init__(ho_ten, nam_sinh)
        self.ma_gv = ma_gv
        self.khoa = khoa
        self.mon_day = []

    def them_mon_day(self, mon):
        self.mon_day.append(mon)

    # Override phương thức của lớp cha
    def gioi_thieu(self):
        base = super().gioi_thieu()
        return f"{base}, giảng viên khoa {self.khoa}"

# Sử dụng
gv = GiangVien("Trần Thị B", 1985, "GV001", "Công nghệ thông tin")
gv.them_mon_day("Python")
gv.them_mon_day("Java")
print(gv.gioi_thieu())

# 4. ENCAPSULATION (ĐÓNG GÓI)
print("\n=== ĐÓNG GÓI ===")

class TaiKhoan:
    """Ví dụ về encapsulation"""

    def __init__(self, so_tai_khoan, chu_tai_khoan):
        self.so_tai_khoan = so_tai_khoan
        self.chu_tai_khoan = chu_tai_khoan
        self._so_du = 0  # Protected attribute (quy ước)
        self.__pin = "1234"  # Private attribute

    # Getter
    @property
    def so_du(self):
        return self._so_du

    # Setter
    @so_du.setter
    def so_du(self, gia_tri):
        if gia_tri >= 0:
            self._so_du = gia_tri
        else:
            print("Số dư không thể âm!")

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self._so_du += so_tien
            print(f"Đã nạp {so_tien:,}đ. Số dư: {self._so_du:,}đ")

    def rut_tien(self, so_tien, ma_pin):
        if ma_pin != self.__pin:
            print("Mã PIN không đúng!")
            return False

        if so_tien > self._so_du:
            print("Số dư không đủ!")
            return False

        self._so_du -= so_tien
        print(f"Đã rút {so_tien:,}đ. Số dư: {self._so_du:,}đ")
        return True

# Sử dụng
tk = TaiKhoan("123456789", "Nguyễn Văn A")
tk.nap_tien(1000000)
tk.rut_tien(500000, "1234")
print(f"Số dư hiện tại: {tk.so_du:,}đ")

# 5. ĐA HÌNH (POLYMORPHISM)
print("\n=== ĐA HÌNH ===")

class DongVat:
    """Lớp cơ sở trừu tượng"""
    def __init__(self, ten):
        self.ten = ten

    def keu(self):
        pass  # Sẽ được override trong lớp con

class Cho(DongVat):
    def keu(self):
        return f"{self.ten} sủa: Gâu gâu!"

class Meo(DongVat):
    def keu(self):
        return f"{self.ten} kêu: Meo meo!"

class Ga(DongVat):
    def keu(self):
        return f"{self.ten} gáy: Ò ó o!"

# Đa hình trong thực tế
def cho_dong_vat_keu(dong_vat):
    """Hàm nhận bất kỳ động vật nào"""
    print(dong_vat.keu())

# Tạo danh sách động vật
zoo = [
    Cho("Cún"),
    Meo("Miu"),
    Ga("Gà trống"),
    Cho("Lucky")
]

# Xử lý đa hình
for dv in zoo:
    cho_dong_vat_keu(dv)

# 6. MAGIC METHODS
print("\n=== MAGIC METHODS ===")

class PhanSo:
    """Class biểu diễn phân số với các magic methods"""

    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self._rut_gon()

    def _rut_gon(self):
        """Rút gọn phân số"""
        from math import gcd
        ucln = gcd(abs(self.tu), abs(self.mau))
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self):
        """Chuyển thành string"""
        if self.mau == 1:
            return str(self.tu)
        return f"{self.tu}/{self.mau}"

    def __add__(self, other):
        """Cộng hai phân số"""
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __mul__(self, other):
        """Nhân hai phân số"""
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __eq__(self, other):
        """So sánh bằng"""
        return self.tu * other.mau == other.tu * self.mau

    def __lt__(self, other):
        """So sánh nhỏ hơn"""
        return self.tu * other.mau < other.tu * self.mau

# Sử dụng
ps1 = PhanSo(1, 2)
ps2 = PhanSo(1, 3)
ps3 = ps1 + ps2

print(f"{ps1} + {ps2} = {ps3}")
print(f"{ps1} * {ps2} = {ps1 * ps2}")
print(f"{ps1} == {ps2}: {ps1 == ps2}")
print(f"{ps1} > {ps2}: {ps1 > ps2}")
