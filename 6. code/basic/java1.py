"""
Viết chương trình tính tổng các số chẵn từ 1 đến 100.
"""


def sum_even_numbers():
    return sum(i for i in range(1, 101) if i % 2 == 0)


if __name__ == "__main__":
    print("Sum 1-100:", sum_even_numbers())
