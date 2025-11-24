
def paginate(query, page: int = 1, page_size: int = 10):
    total_items = query.count()
 
    
    if page == None:
        page = 1
    if page_size == None:
        page_size = total_items

    page = int(page)
    page_size = int(page_size)

    total_pages = (total_items + page_size - 1) // page_size

    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()

    return {
        "items": items,
        "page": page,
        "page_size": page_size,
        "total_items": total_items,
        "total_pages": total_pages,
    }
