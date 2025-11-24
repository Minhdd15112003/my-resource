file_path = "file.deb"  # Thay bằng đường dẫn file thực tế
chunk_size = 200_000  # 200KB

with open(file_path, "rb") as f:
    chunk_number = 0
    while True:
        chunk = f.read(chunk_size)  # Đọc 200KB
        if not chunk:  # Nếu không còn dữ liệu
            break
        # Gửi chunk dưới dạng byte
        sio.emit("message", {
            "status": "chunk",
            "chunk_number": chunk_number,
            "data": chunk
        })
        chunk_number += 1