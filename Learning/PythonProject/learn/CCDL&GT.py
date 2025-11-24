# cấu trúc dữ liệu ngăn xếp

# def A():
#     print("A")
#
# def B():
#     A()
#     print("B")
#
# if __name__ == "__main__":
#   B()

# Đệ quy

def factorial(n):
    if n == 0 or n == 1:  # Trường hợp cơ bản
        return 1

    return n * factorial(n - 1)


# sum(5) = 5 + sum(4)
#        = 5 + (4 + sum(3))
#        = 5 + (4 + (3 + sum(2)))
#        = 5 + (4 + (3 + (2 + sum(1))))
#        = 5 + (4 + (3 + (2 + (1 + sum(0)))))
#        = 5 + (4 + (3 + (2 + (1 + 0))))
#        = 5 + (4 + (3 + (2 + 1)))
#        = 5 + (4 + (3 + 3))
#        = 5 + (4 + 6)
#        = 5 + 10
#        = 15

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n - 1)

# Đổ phức tạp của thuật toán O()
if __name__ == "__main__":
    print(5 * (5 + 1) // 2)



# 1 2 3 4 5 6 7 8 9
#
# 10
# 10
# 10
# 10