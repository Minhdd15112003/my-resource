import threading


def lay_so_chan(number):
    if number % 2 == 0:
        print(number)


if __name__ == '__main__':
    num_thread = int(input("set number thread: "))
    data = [32, 56, 87, 90, 0, 1, 12, 54, 77, 9, 87, 45, 123, 68, 9, 43, 67, 98, 23, 3, 3645, 7558, 6, 978, 78, 0, 5,
            67, 45, 63456, 8, 6, 785, 324, 867, 6, 45, 6, 556, 4, 45, 745, 8, 45, 43, 5, 21, 3, 534, 45, 34, 6, 346, 46,
            43, 6]

    thread = len(data) // num_thread
    # offset = (num_thread - 1) * thread
    for i in range(1, num_thread + 1):
        print((i - 1) * thread)

