from marshmallow import fields, validate
from marshmallow_mongoengine import ModelSchema

from app.model import Student, Books, Author, Category, Borrow


class BooksSchema(ModelSchema):
    class Meta:
        model = Books
        load_instance = True

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    page_count = fields.Int()


class StudentSchema(ModelSchema):
    class Meta:
        model = Student
        load_instance = True

    # Dump only fields (chỉ xuất ra, không nhận vào)
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    birth_date = fields.DateTime(required=False)
    gender = fields.Str(
        required=True, validate=validate.OneOf(["male", "female", "other"])
    )
    class_name = fields.Str(required=True, validate=validate.Length(max=10))


class AuthorSchema(ModelSchema):
    class Meta:
        model = Author
        load_instance = True

    # Dump only fields (chỉ xuất ra, không nhận vào)
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    # Liên kết quan hệ một-nhiều với Books
    books = fields.Nested(BooksSchema, many=True, dump_only=True)


class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        load_instance = True

    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(required=False)
    # Liên kết quan hệ một-nhiều với Books
    books = fields.Nested(BooksSchema, many=True, dump_only=True)


class BorrowSchema(ModelSchema):
    class Meta:
        model = Borrow
        load_instance = True

    id = fields.Str(dump_only=True)
    book = fields.Nested(BooksSchema, required=True)
    student = fields.Nested(StudentSchema, required=True)
    borrow_date = fields.DateTime()
    return_date = fields.DateTime()
