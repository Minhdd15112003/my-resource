"""
Query Builder Utility for SQLAlchemy
Hỗ trợ filter động cho bất kỳ model và trường nào
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Type, Callable
from flask import request
from sqlalchemy import or_
from sqlalchemy.orm.query import Query

from app.core.utils.paging import Paging
from app.core.database.mysql.database import db


class QueryBuilder:
    """
    Query Builder để tạo query động với filter linh hoạt cho SQLAlchemy

    Hỗ trợ các kiểu filter:
    - exact: So sánh chính xác (=)
    - icontains: Chứa chuỗi (case-insensitive)
    - istartswith: Bắt đầu bằng (case-insensitive)
    - iendswith: Kết thúc bằng (case-insensitive)
    - gt: Lớn hơn (>)
    - gte: Lớn hơn hoặc bằng (>=)
    - lt: Nhỏ hơn (<)
    - lte: Nhỏ hơn hoặc bằng (<=)
    - in: Nằm trong danh sách
    - ne: Không bằng (!=)
    """

    # Các operator được hỗ trợ
    OPERATORS = [
        "exact",
        "icontains",
        "contains",
        "istartswith",
        "iendswith",
        "startswith",
        "endswith",
        "gt",
        "gte",
        "lt",
        "lte",
        "in",
        "ne",
    ]

    @staticmethod
    def parse_date_range(
        date_string: str, is_end_date: bool = False
    ) -> Optional[datetime]:
        """
        Parse date string for date range filtering

        Args:
            date_string: Date string to parse
            is_end_date: If True, set time to end of day for date-only strings

        Returns:
            Parsed datetime object or None if parsing fails
        """
        if not date_string:
            return None

        try:
            # Try different date formats
            for fmt in [
                "%Y-%m-%dT%H:%M:%S.%f",  # 2023-12-25T14:30:45.123456
                "%Y-%m-%dT%H:%M:%S",  # 2023-12-25T14:30:45
                "%Y-%m-%d %H:%M:%S",  # 2023-12-25 14:30:45
                "%Y-%m-%d",  # 2023-12-25
                "%d/%m/%Y",  # 25/12/2023
                "%d-%m-%Y",  # 25-12-2023
            ]:
                try:
                    parsed_date = datetime.strptime(date_string, fmt)

                    # If it's a date-only format and this is an end date, set to end of day
                    if is_end_date and fmt in ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]:
                        parsed_date = parsed_date.replace(
                            hour=23, minute=59, second=59, microsecond=999999
                        )

                    return parsed_date
                except ValueError:
                    continue

            return None
        except Exception:
            return None

    @staticmethod
    def parse_value(value: Any, field_type: str = "auto") -> Any:
        """
        Parse giá trị từ request theo kiểu dữ liệu

        Args:
            value: Giá trị cần parse
            field_type: Kiểu dữ liệu ('string', 'int', 'float', 'bool', 'date', 'datetime', 'list', 'auto')

        Returns:
            Giá trị đã được parse
        """
        if value is None or value == "":
            return None

        try:
            # Auto detect type
            if field_type == "auto":
                # Check if boolean
                if isinstance(value, str) and value.lower() in ["true", "false"]:
                    return value.lower() == "true"

                # Check if number
                if isinstance(value, str):
                    if value.isdigit():
                        return int(value)
                    try:
                        return float(value)
                    except:
                        pass

                # Check if date/datetime
                if isinstance(value, str):
                    for fmt in [
                        "%Y-%m-%dT%H:%M:%S",
                        "%Y-%m-%dT%H:%M:%S.%f",
                        "%Y-%m-%d",
                    ]:
                        try:
                            return datetime.strptime(value, fmt)
                        except:
                            continue

                return value

            # Explicit type conversion
            if field_type == "int":
                return int(value)
            elif field_type == "float":
                return float(value)
            elif field_type == "bool":
                if isinstance(value, str):
                    return value.lower() in ["true", "1", "yes"]
                return bool(value)
            elif field_type in ["date", "datetime"]:
                if isinstance(value, str):
                    for fmt in [
                        "%Y-%m-%dT%H:%M:%S",
                        "%Y-%m-%dT%H:%M:%S.%f",
                        "%Y-%m-%d",
                    ]:
                        try:
                            return datetime.strptime(value, fmt)
                        except:
                            continue
                return value
            elif field_type == "list":
                if isinstance(value, str):
                    return [v.strip() for v in value.split(",")]
                return value if isinstance(value, list) else [value]
            else:
                return value

        except Exception:
            return value

    @staticmethod
    def apply_filter(
        query: Query, model: Type, field_name: str, operator: str, value: Any
    ) -> Query:
        """
        Apply a single filter condition to query

        Args:
            query: SQLAlchemy Query object
            model: SQLAlchemy Model class
            field_name: Name of the field to filter
            operator: Filter operator
            value: Filter value

        Returns:
            Query with filter applied
        """
        if not hasattr(model, field_name):
            return query

        field = getattr(model, field_name)

        if operator == "exact" or operator == "":
            return query.filter(field == value)
        elif operator == "icontains":
            return query.filter(field.ilike(f"%{value}%"))
        elif operator == "contains":
            return query.filter(field.like(f"%{value}%"))
        elif operator == "istartswith":
            return query.filter(field.ilike(f"{value}%"))
        elif operator == "iendswith":
            return query.filter(field.ilike(f"%{value}"))
        elif operator == "startswith":
            return query.filter(field.like(f"{value}%"))
        elif operator == "endswith":
            return query.filter(field.like(f"%{value}"))
        elif operator == "gt":
            return query.filter(field > value)
        elif operator == "gte":
            return query.filter(field >= value)
        elif operator == "lt":
            return query.filter(field < value)
        elif operator == "lte":
            return query.filter(field <= value)
        elif operator == "in":
            if isinstance(value, str):
                value = [v.strip() for v in value.split(",")]
            return query.filter(field.in_(value))
        elif operator == "ne":
            return query.filter(field != value)
        else:
            return query

    @staticmethod
    def build_filters(model: Type, filters: Dict[str, Any]) -> Query:
        """
        Build SQLAlchemy query from filters dictionary

        Args:
            model: SQLAlchemy Model class
            filters: Dictionary of filters

        Returns:
            Query object with filters applied
        """
        query = db.session.query(model)
        type_hints = {}

        # Extract type hints first
        for key, value in filters.items():
            if key.endswith("__type"):
                field_name = key.replace("__type", "")
                type_hints[field_name] = value

        # Build filters
        for key, value in filters.items():
            if value is None or value == "" or key.endswith("__type"):
                continue

            # Parse field name and operator
            parts = key.split("__")
            field_name = parts[0]

            # Check if operator is explicitly specified
            has_explicit_operator = (
                len(parts) > 1 and parts[1] in QueryBuilder.OPERATORS
            )
            operator = parts[1] if has_explicit_operator else None

            # Get type hint
            field_type = type_hints.get(field_name, "auto")

            # Parse value
            parsed_value = QueryBuilder.parse_value(value, field_type)

            if parsed_value is not None:
                # Auto-detect operator based on value type if not explicitly set
                if operator is None:
                    if isinstance(parsed_value, str):
                        operator = "icontains"
                    else:
                        operator = "exact"

                # Apply filter
                query = QueryBuilder.apply_filter(
                    query, model, field_name, operator, parsed_value
                )

        return query

    @staticmethod
    def apply_filters(
        model: Type,
        filters: Optional[Dict[str, Any]] = None,
        search_fields: Optional[List[str]] = None,
        search_query: Optional[str] = None,
    ) -> Query:
        """
        Apply filters to a SQLAlchemy model query

        Args:
            model: SQLAlchemy Model class
            filters: Dictionary of filters to apply
            search_fields: List of fields to search in (for search_query)
            search_query: Search string to search across multiple fields

        Returns:
            Query with filters applied
        """
        query = QueryBuilder.build_filters(model, filters or {})

        # Apply search across multiple fields (OR condition)
        if search_query and search_fields:
            search_conditions = []
            for field_name in search_fields:
                if hasattr(model, field_name):
                    field = getattr(model, field_name)
                    search_conditions.append(field.ilike(f"%{search_query}%"))

            if search_conditions:
                query = query.filter(or_(*search_conditions))

        return query

    @staticmethod
    def find_all_with_filters(
        model: Type,
        schema: Any,
        filters: Optional[Dict[str, Any]] = None,
        search_fields: Optional[List[str]] = None,
        default_order_by: str = "-created_at",
        custom_processor: Optional[Callable] = None,
    ) -> Dict[str, Any]:
        """
        Find all records with filters, pagination, search, and date range support

        Args:
            model: SQLAlchemy Model class
            schema: Marshmallow Schema for serialization
            filters: Dictionary of filters to apply
            search_fields: List of fields to search in (for search_query)
            default_order_by: Default ordering field (prefix with '-' for desc)
            custom_processor: Optional function to process data before return

        URL Parameters supported:
            - page: Page number (default: 1)
            - limit: Records per page (default: 10)
            - order_by: Field to order by (prefix with '-' for desc)
            - search: Search query across search_fields
            - from_date: Start date for created_at filtering (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)
            - to_date: End date for created_at filtering (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)

        Date Range Examples:
            - ?from_date=2023-12-01&to_date=2023-12-31 (filter by date range)
            - ?from_date=2023-12-01T10:30:00 (from specific datetime)
            - ?to_date=2023-12-31 (up to end of day)

        Returns:
            Dictionary with data, pagination info, and counts
        """

        # Get pagination params
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))
        order_by = request.args.get("order_by", default_order_by)
        search = request.args.get("search", None)

        # Get date range params for created_at filtering
        from_date = request.args.get("from_date", None)
        to_date = request.args.get("to_date", None)

        # Use provided filters or get from request
        if filters is None:
            filters = request.args.to_dict()

        # Remove pagination params and date range params from filters
        filters = {
            k: v
            for k, v in filters.items()
            if k not in ["page", "limit", "order_by", "search", "from_date", "to_date"]
        }

        # Apply filters
        query = QueryBuilder.apply_filters(
            model=model,
            filters=filters,
            search_fields=search_fields,
            search_query=search,
        )

        # Apply date range filtering for created_at
        if hasattr(model, "created_at"):
            if from_date:
                parsed_from_date = QueryBuilder.parse_date_range(
                    from_date, is_end_date=False
                )
                if parsed_from_date:
                    query = query.filter(model.created_at >= parsed_from_date)

            if to_date:
                parsed_to_date = QueryBuilder.parse_date_range(
                    to_date, is_end_date=True
                )
                if parsed_to_date:
                    query = query.filter(model.created_at <= parsed_to_date)

        # Count total
        total_count = query.count()

        # Apply pagination
        paging = Paging(limit=limit, page=page, count=total_count)
        paging.process()

        # Apply ordering
        if order_by:
            if order_by.startswith("-"):
                # Descending order
                field_name = order_by[1:]
                if hasattr(model, field_name):
                    query = query.order_by(getattr(model, field_name).desc())
            else:
                # Ascending order
                if hasattr(model, order_by):
                    query = query.order_by(getattr(model, order_by).asc())

        # Execute query with pagination
        results = query.offset(paging.skip).limit(paging.limit).all()

        # Dump to schema
        data = schema.dump(results)

        # Apply custom processor if provided
        if custom_processor and callable(custom_processor):
            data = custom_processor(data)

        return {
            "data": data,
            "count": paging.count,
            "total_pages": paging.total_pages,
            "page": paging.page,
            "limit": paging.limit,
        }

    @staticmethod
    def find_one_with_filters(
        model: Type,
        schema: Any,
        filters: Dict[str, Any],
    ) -> Optional[Dict[str, Any]]:
        """
        Tìm một record duy nhất với filters

        Args:
            model: SQLAlchemy Model class
            schema: Marshmallow Schema
            filters: Dictionary of filters

        Returns:
            Dictionary with data or None
        """
        query = QueryBuilder.apply_filters(model=model, filters=filters)
        result = query.first()

        if result:
            return schema.dump(result)
        return None
