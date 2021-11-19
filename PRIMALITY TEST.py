from math import factorial


def is_wprime(n):
    return n > 1 and bool(n == 2 or
                          (n % 2 and (factorial(n - 1) + 1) % n == 0))


if __name__ == '__main__':
    c = 8
    print(f"Primes under {c}:", end='\n  ')
    print([n for n in range(c) if is_wprime(n)])
    """
    __main__ digunakan ketika kita berkerja dengan menggunakan modul,
    disini kita menggunakan modul math
    """
