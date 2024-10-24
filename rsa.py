import random

# Các số nguyên tố nhỏ để tăng tốc kiểm tra số nguyên tố cho các giá trị nhỏ
lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
             73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
             157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
             239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
             331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
             421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
             509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
             613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
             709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
             821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
             919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def generateLargePrime(keysize):
    """
    Hàm tạo số nguyên tố lớn với kích thước keysize bit
    """
    while True:
        # Tạo số ngẫu nhiên có kích thước bit là keysize
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        # Kiểm tra xem số này có phải là số nguyên tố không
        if (isPrime(num)):
            return num


def rabinMiller(n, d):
    # Chọn ngẫu nhiên a, x = a^d % n
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)

    # Nếu x = 1 hoặc x = n - 1, có thể n là số nguyên tố
    if x == 1 or x == n - 1:
        return True

    # Bình phương x và kiểm tra tính nguyên tố
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        elif x == n - 1:
            return True

    # Trả về False nếu không phải số nguyên tố
    return False


def isPrime(n):
    """
    Hàm kiểm tra số nguyên tố:
    - Trả về True nếu n là số nguyên tố
    - Sử dụng thuật toán rabinMiller nếu không chắc chắn
    """
    # Các số nhỏ hơn 2 không phải là số nguyên tố
    if n < 2:
        return False

    # Nếu n nằm trong danh sách các số nguyên tố nhỏ
    if n in lowPrimes:
        return True

    # Kiểm tra nếu n chia hết cho bất kỳ số nguyên tố nhỏ nào
    for prime in lowPrimes:
        if n % prime == 0:
            return False

    # Tìm c sao cho c * 2^r = n - 1 (c là số lẻ)
    c = n - 1
    while c % 2 == 0:
        c /= 2

    # Chạy thuật toán rabinMiller 128 lần để kiểm tra
    for i in range(128):
        if not rabinMiller(n, c):
            return False

    return True


def generateKeys(keysize=1024):
    """
    Hàm tạo khóa RSA với kích thước keysize bit
    Trả về các giá trị p, q, e, d, N
    """
    e = d = N = 0

    # Tạo 2 số nguyên tố p và q
    p = generateLargePrime(keysize)
    q = generateLargePrime(keysize)

    # Tính N = p * q và phiN = (p-1) * (q-1)
    N = p * q
    phiN = (p - 1) * (q - 1)

    # Chọn e sao cho e là số nguyên tố cùng nhau với phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break

    # Tính d là nghịch đảo modular của e với phiN
    d = modularInv(e, phiN)

    return p, q, e, d, N


def isCoPrime(p, q):
    """
    Kiểm tra xem p và q có phải là số nguyên tố cùng nhau (gcd(p, q) = 1)
    """
    return gcd(p, q) == 1


def gcd(p, q):
    """
    Thuật toán Euclid để tìm ước chung lớn nhất (gcd) của p và q
    """
    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    """
    Thuật toán Euclid mở rộng để tìm (gcd, x, y) sao cho ax + by = gcd(a, b)
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def modularInv(a, b):
    """
    Tìm nghịch đảo modular của a với modulo b bằng cách sử dụng thuật toán Euclid mở rộng
    """
    gcd, x, y = egcd(a, b)
    if x < 0:
        x += b
    return x


class RSA(object):
    """
    Lớp RSA dùng để mã hóa và giải mã thông điệp
    """

    def __init__(self, keysize=1024):
        # Khởi tạo với keysize và tạo khóa RSA
        self.keysize = keysize
        self.p, self.q, self.e, self.d, self.N = generateKeys(self.keysize)

    def encrypt(self, msg):
        """
        Mã hóa thông điệp
        """
        cipher = ""

        # Chuyển mỗi ký tự thành mã ASCII, sau đó mã hóa
        for c in msg:
            m = ord(c)
            cipher += str(pow(m, self.e, self.N)) + " "

        return cipher

    def decrypt(self, cipher):
        """
        Giải mã thông điệp
        """
        msg = ""
        parts = cipher.split()

        # Giải mã từng phần của cipher và chuyển lại thành ký tự
        for part in parts:
            if part:
                c = int(part)
                msg += chr(pow(c, self.d, self.N))

        return msg


if __name__ == "__main__":
    print("Demo mã hóa RSA")

    # Nhập thông điệp và thực hiện mã hóa, giải mã
    msg = input("Nhập message: ")
    rsa = RSA(keysize=32)
    enc = rsa.encrypt(msg=msg)
    dec = rsa.decrypt(cipher=enc)

    # In kết quả mã hóa và giải mã
    print(f"Message: {msg}")
    print(f"e: {rsa.e}")
    print(f"d: {rsa.d}")
    print(f"N: {rsa.N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")
