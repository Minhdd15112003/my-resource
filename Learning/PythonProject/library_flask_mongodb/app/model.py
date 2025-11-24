from datetime import datetime

from mongoengine import StringField, Document, IntField, DateTimeField, ReferenceField, ObjectIdField


# Document cho Author - tác giả sách
class Author(Document):
    name = StringField(
        required=True,
        min_length=2,
        max_length=100
    )
    meta = {'collection': 'authors'}


# Document cho Category - danh mục sách
class Category(Document):
    name = StringField(
        required=True,
        min_length=2,
        max_length=50
    )
    description = StringField(max_length=200)

    meta = {'collection': 'categories'}


# Document cho Student - học sinh
class Student(Document):
    name = StringField(
        required=True,
        min_length=3,
        max_length=50,
        regex=r'^[a-zA-Z0-9_]+$'
    )
    birth_date = DateTimeField(
        null=True
    )
    gender = StringField(choices=('male', 'female', 'other'))
    class_name = StringField(
        max_length=10
    )

    meta = {
        'collection': 'students',
        # Tạo index để tối ưu query
        'indexes': ['name', 'class_name']
    }


# Document cho Books - sách
class Books(Document):
    id = ObjectIdField(db_field="_id")
    name = StringField(
        required=True,
        min_length=3,
        max_length=50,
        regex=r'^[a-zA-Z0-9_]+$'
    )
    page_count = IntField()

    # MỐI QUAN HỆ: Books -> Author (Many-to-One)
    # Nhiều sách có thể thuộc về một tác giả
    # ReferenceField tạo liên kết với Author document
    author = ReferenceField(
        Author,
        required=False,
        reverse_delete_rule=2  # CASCADE - xóa author thì xóa luôn books
    )
    # MỐI QUAN HỆ: Books -> Category (Many-to-One)
    # Nhiều sách có thể thuộc về một danh mục
    category = ReferenceField(
        Category,
        required=False,
        reverse_delete_rule=3  # NULLIFY - set category thành null nếu category bị xóa
    )

    meta = {
        'collection': 'books',
        # Tạo index để tối ưu query
        'indexes': ['name', 'author', 'category']
    }

    def __str__(self):
        return f"Books{self.id}"


# Document cho Borrow - mượn sách
# Đây là bảng trung gian để tạo mối quan hệ Many-to-Many giữa Student và Books
class Borrow(Document):
    # MỐI QUAN HỆ: Borrow -> Books (Many-to-One)
    # Nhiều lần mượn có thể cùng một cuốn sách
    # reverse_delete_rule=1 (DENY) - không cho xóa book nếu còn borrow records
    # Điều này đảm bảo tính toàn vẹn dữ liệu
    book = ReferenceField(
        Books,
        required=True,
        reverse_delete_rule=1  # DENY - không cho xóa book nếu còn borrow records
    )

    # MỐI QUAN HỆ: Borrow -> Student (Many-to-One)
    # Nhiều lần mượn có thể thuộc về một học sinh
    # reverse_delete_rule=2 (CASCADE) - xóa student thì xóa luôn borrow records
    # Khi học sinh rời trường thì xóa luôn lịch sử mượn sách
    student = ReferenceField(
        Student,
        required=True,
        reverse_delete_rule=2  # CASCADE - xóa student thì xóa luôn borrow records
    )

    borrow_date = DateTimeField(default=datetime.now)
    return_date = DateTimeField(null=True)

    meta = {
        'collection': 'borrows',
        # Tạo index để tối ưu query
        'indexes': [
            'student',
            'book',
            'borrow_date',
        ]
    }

# TỔNG QUAN CÁC MỐI QUAN HỆ:
# 1. Author (1) ----< Books (N): Một tác giả có thể viết nhiều sách
# 2. Student (1) ----< Borrow (N): Một học sinh có thể mượn nhiều lần
# 3. Books (1) ----< Borrow (N): Một cuốn sách có thể được mượn nhiều lần
# 4. Student (N) ----< Borrow >---- Books (N): Many-to-Many qua bảng Borrow
# 5. Category (1) ----< Books (N): Một danh mục có thể có nhiều sách
#    Một học sinh có thể mượn nhiều sách, một sách có thể được nhiều học sinh mượn (ở các thời điểm khác nhau)

# REVERSE DELETE RULES:
# - CASCADE (2): Khi xóa parent, tự động xóa tất cả child records
# - DENY (1): Không cho phép xóa parent nếu còn child records
# - NULLIFY (3): Set reference field thành null khi parent bị xóa
# - PULL (4): Remove reference từ list field khi parent bị xóa
