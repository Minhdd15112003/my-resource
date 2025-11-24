# 📚 QueryBuilder Documentation

## 🔍 Tổng quan

`QueryBuilder` là một utility class mạnh mẽ cho SQLAlchemy, giúp tạo các query động với khả năng filter linh hoạt, pagination, search và date range filtering.

## 🚀 Tính năng chính

- ✅ **Dynamic Filtering**: Filter động với nhiều operators
- ✅ **Pagination**: Phân trang tự động
- ✅ **Search**: Tìm kiếm trên nhiều trường
- ✅ **Date Range**: Lọc theo khoảng thời gian
- ✅ **Type Parsing**: Tự động parse kiểu dữ liệu
- ✅ **Ordering**: Sắp xếp linh hoạt

---

## 📖 Các Phương thức

### 1. `parse_date_range(date_string, is_end_date=False)`

Parse chuỗi ngày tháng cho việc lọc theo khoảng thời gian.

**Tham số:**

- `date_string`: Chuỗi ngày cần parse
- `is_end_date`: Nếu True, sẽ set thời gian về cuối ngày cho format chỉ có ngày

**Định dạng hỗ trợ:**

```python
# ISO formats
"2023-12-25T14:30:45.123456"  # Với microseconds
"2023-12-25T14:30:45"         # ISO standard
"2023-12-25 14:30:45"         # Space separated

# Date only formats
"2023-12-25"                  # YYYY-MM-DD
"25/12/2023"                  # DD/MM/YYYY
"25-12-2023"                  # DD-MM-YYYY
```

**Ví dụ:**

```python
# Parse ngày bắt đầu
start_date = QueryBuilder.parse_date_range("2023-12-01")
# Result: 2023-12-01 00:00:00

# Parse ngày kết thúc (tự động set cuối ngày)
end_date = QueryBuilder.parse_date_range("2023-12-31", is_end_date=True)
# Result: 2023-12-31 23:59:59.999999
```

---

### 2. `parse_value(value, field_type="auto")`

Parse giá trị từ request theo kiểu dữ liệu.

**Kiểu dữ liệu hỗ trợ:**

- `auto`: Tự động detect kiểu
- `string`: Chuỗi
- `int`: Số nguyên
- `float`: Số thực
- `bool`: Boolean
- `date/datetime`: Ngày tháng
- `list`: Danh sách

**Ví dụ:**

```python
# Auto detection
QueryBuilder.parse_value("123")        # → 123 (int)
QueryBuilder.parse_value("12.34")      # → 12.34 (float)
QueryBuilder.parse_value("true")       # → True (bool)
QueryBuilder.parse_value("2023-12-25") # → datetime object

# Explicit type
QueryBuilder.parse_value("1,2,3", "list")  # → ["1", "2", "3"]
QueryBuilder.parse_value("yes", "bool")     # → True
```

---

### 3. `apply_filter(query, model, field_name, operator, value)`

Áp dụng một filter condition vào query.

**Operators hỗ trợ:**

| Operator      | Mô tả                                      | Ví dụ                       |
| ------------- | ------------------------------------------ | --------------------------- |
| `exact`       | So sánh chính xác (=)                      | `name__exact=John`          |
| `icontains`   | Chứa chuỗi (không phân biệt hoa thường)    | `name__icontains=john`      |
| `contains`    | Chứa chuỗi (phân biệt hoa thường)          | `name__contains=John`       |
| `istartswith` | Bắt đầu bằng (không phân biệt hoa thường)  | `name__istartswith=jo`      |
| `iendswith`   | Kết thúc bằng (không phân biệt hoa thường) | `name__iendswith=hn`        |
| `startswith`  | Bắt đầu bằng (phân biệt hoa thường)        | `name__startswith=Jo`       |
| `endswith`    | Kết thúc bằng (phân biệt hoa thường)       | `name__endswith=hn`         |
| `gt`          | Lớn hơn (>)                                | `age__gt=18`                |
| `gte`         | Lớn hơn hoặc bằng (>=)                     | `age__gte=18`               |
| `lt`          | Nhỏ hơn (<)                                | `age__lt=65`                |
| `lte`         | Nhỏ hơn hoặc bằng (<=)                     | `age__lte=65`               |
| `in`          | Nằm trong danh sách                        | `status__in=active,pending` |
| `ne`          | Không bằng (!=)                            | `status__ne=inactive`       |

**Ví dụ:**

```python
# Tìm users có tên chứa "John"
query = QueryBuilder.apply_filter(
    query=query,
    model=User,
    field_name="full_name",
    operator="icontains",
    value="John"
)

# Tìm users có tuổi >= 18
query = QueryBuilder.apply_filter(
    query=query,
    model=User,
    field_name="age",
    operator="gte",
    value=18
)
```

---

### 4. `build_filters(model, filters)`

Build SQLAlchemy query từ filters dictionary.

**Type hints:**
Sử dụng `field__type` để chỉ định kiểu dữ liệu:

```python
filters = {
    "age": "25",
    "age__type": "int",
    "created_at": "2023-12-25",
    "created_at__type": "datetime",
    "tags": "python,flask,api",
    "tags__type": "list"
}
```

**Ví dụ:**

```python
filters = {
    "full_name__icontains": "John",
    "age__gte": "18",
    "status__in": "active,pending",
    "is_active": "true"
}

query = QueryBuilder.build_filters(User, filters)
```

---

### 5. `apply_filters(model, filters, search_fields, search_query)`

Áp dụng filters và search vào SQLAlchemy model query.

**Tham số:**

- `model`: SQLAlchemy Model class
- `filters`: Dictionary của filters
- `search_fields`: Danh sách fields để search
- `search_query`: Chuỗi search

**Ví dụ:**

```python
# Search "john" trong các trường full_name, email, username
query = QueryBuilder.apply_filters(
    model=User,
    filters={"status": "active"},
    search_fields=["full_name", "email", "username"],
    search_query="john"
)
```

---

### 6. `find_all_with_filters()` ⭐ (Phương thức chính)

Tìm tất cả records với filters, pagination, search và date range.

**Tham số:**

- `model`: SQLAlchemy Model class
- `schema`: Marshmallow Schema cho serialization
- `filters`: Dictionary của filters (tùy chọn)
- `search_fields`: Danh sách fields để search
- `default_order_by`: Field mặc định để sắp xếp
- `custom_processor`: Function xử lý data trước khi return

**URL Parameters:**

| Parameter   | Mô tả                                  | Ví dụ                   |
| ----------- | -------------------------------------- | ----------------------- |
| `page`      | Số trang (mặc định: 1)                 | `?page=2`               |
| `limit`     | Số records/trang (mặc định: 10)        | `?limit=20`             |
| `order_by`  | Field để sắp xếp (prefix '-' cho desc) | `?order_by=-created_at` |
| `search`    | Chuỗi search                           | `?search=john`          |
| `from_date` | Ngày bắt đầu filter                    | `?from_date=2023-12-01` |
| `to_date`   | Ngày kết thúc filter                   | `?to_date=2023-12-31`   |

**Ví dụ sử dụng trong Service:**

```python
from app.core.utils.query_builder import QueryBuilder
from app.domain.users.model import User
from app.domain.users.schema import UserSchema

class UserService:
    @staticmethod
    def find_all():
        return QueryBuilder.find_all_with_filters(
            model=User,
            schema=UserSchema(many=True),
            search_fields=["full_name", "email", "username"],
            default_order_by="-created_at"
        )
```

---

### 7. `find_one_with_filters(model, schema, filters)`

Tìm một record duy nhất với filters.

**Ví dụ:**

```python
user = QueryBuilder.find_one_with_filters(
    model=User,
    schema=UserSchema(),
    filters={"email": "john@example.com"}
)
```

---

## 🌐 Ví dụ URL thực tế

### **Basic Filtering:**

```
# Tìm users active
GET /api/user?status=active

# Tìm users có tên chứa "John"
GET /api/user?full_name__icontains=john

# Tìm users có tuổi >= 18
GET /api/user?age__gte=18

# Tìm users với nhiều status
GET /api/user?status__in=active,pending
```

### **Pagination:**

```
# Trang 2, 20 records/trang
GET /api/user?page=2&limit=20

# Sắp xếp theo tên (A-Z)
GET /api/user?order_by=full_name

# Sắp xếp theo ngày tạo (mới nhất)
GET /api/user?order_by=-created_at
```

### **Search:**

```
# Tìm "john" trong tên, email, username
GET /api/user?search=john

# Kết hợp search và filter
GET /api/user?search=john&status=active
```

### **Date Range Filtering:**

```
# Users tạo trong tháng 12/2023
GET /api/user?from_date=2023-12-01&to_date=2023-12-31

# Users tạo từ ngày cụ thể
GET /api/user?from_date=2023-12-01T10:30:00

# Users tạo trước ngày nhất định
GET /api/user?to_date=2023-12-31

# Kết hợp date range với filters khác
GET /api/user?from_date=2023-12-01&to_date=2023-12-31&status=active&search=john
```

### **Complex Filtering:**

```
# Tìm users active, có email gmail, tạo trong Q4 2023
GET /api/user?status=active&email__icontains=gmail&from_date=2023-10-01&to_date=2023-12-31

# Pagination + Search + Date Range + Multiple Filters
GET /api/user?page=1&limit=25&search=john&status__in=active,pending&from_date=2023-01-01&order_by=-created_at
```

---

## 💡 Tips và Best Practices

### **1. Type Hints:**

Sử dụng type hints khi cần parse chính xác:

```python
# Trong request body hoặc URL params
{
    "age": "25",
    "age__type": "int",
    "is_active": "true",
    "is_active__type": "bool"
}
```

### **2. Custom Processing:**

```python
def custom_processor(data):
    # Thêm computed fields
    for item in data:
        item['display_name'] = f"{item['full_name']} ({item['email']})"
    return data

result = QueryBuilder.find_all_with_filters(
    model=User,
    schema=UserSchema(many=True),
    custom_processor=custom_processor
)
```

### **3. Error Handling:**

QueryBuilder tự động handle errors:

- Invalid date formats → bỏ qua
- Invalid field names → bỏ qua
- Parse errors → sử dụng giá trị gốc

### **4. Performance:**

- Sử dụng indexes trên các fields thường filter
- Limit page size hợp lý (10-50 records)
- Avoid search trên text fields lớn

---

## 🔧 Response Format

```json
{
    "data": [...],           // Danh sách records
    "count": 15,             // Số records hiện tại
    "total_pages": 3,        // Tổng số trang
    "page": 1,               // Trang hiện tại
    "limit": 10              // Số records/trang
}
```

---

## ⚠️ Lưu ý

1. **Date Range chỉ áp dụng cho `created_at`** - nếu cần filter date khác, sử dụng operators `gt`, `gte`, `lt`, `lte`
2. **Search fields** phải được định nghĩa trong service
3. **Operators** phân biệt hoa thường trừ `icontains`, `istartswith`, `iendswith`
4. **Type conversion** an toàn - không throw exception nếu parse fail
5. **Pagination** bắt đầu từ page 1

---

Tài liệu này cung cấp hướng dẫn đầy đủ để sử dụng QueryBuilder một cách hiệu quả! 🚀
