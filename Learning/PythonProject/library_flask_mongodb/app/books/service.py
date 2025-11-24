from flask import request, jsonify
from marshmallow import ValidationError

from app.model import Books
from schemas import BooksSchema

book_schema = BooksSchema()
books_schema = BooksSchema(many=True)


def get_all_books():
    try:
        list_book = Books.objects.all()
        result = books_schema.dump(list_book)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def insert_book():
    try:
        json_data = request.get_json()
        if not json_data:
            return jsonify({'error': 'No JSON data provided'}), 400
        # Load và validate data với schema
        validated_book_data = book_schema.load(json_data)

        new_book = validated_book_data.save()
        serialized_result = book_schema.dump(new_book)

        return jsonify({"result": serialized_result}), 201
    except ValidationError as e:
        return jsonify({'errors': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_book_by_id(book_id):
    try:
        book = Books.objects(id=book_id).first()
        if not book:
            return jsonify({'error': 'Book not found'}), 404
        result = book_schema.dump(book)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_book(book_id):
    try:
        json_data = request.get_json()
        if not json_data:
            return jsonify({'error': 'No JSON data provided'}), 400

        book = Books.objects(id=book_id).first()
        if not book:
            return jsonify({'error': 'Book not found'}), 404

        # Load và validate data với schema
        validated_book_data = book_schema.load(json_data, partial=True)

        # Cập nhật các trường đã được xác thực
        for key, value in validated_book_data.items():
            setattr(book, key, value)  # setattr dùng để gán giá trị cho thuộc tính của đối tượng

        updated_book = book.save()
        serialized_result = book_schema.dump(updated_book)

        return jsonify({"result": serialized_result})
    except ValidationError as e:
        return jsonify({'errors': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
