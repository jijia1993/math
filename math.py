# 数学工具集 - 基础计算与数论算法
import math

# 1. 基础计算函数
def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算（除0会抛出异常）"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b

def power(a, n):
    """计算a的n次幂"""
    return a ** n

def factorial(n):
    """计算n的阶乘（n≥0）"""
    if n < 0:
        raise ValueError("阶乘仅对非负整数有定义")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 2. 数论核心算法
def is_prime(n):
    """判断n是否为素数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """计算a和b的最大公约数（欧几里得算法）"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算a和b的最小公倍数"""
    return a * b // gcd(a, b)

def factorize(n):
    """质因数分解，返回因数列表"""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# 3. 测试代码（运行时会输出结果）
if __name__ == "__main__":
    print("=== 基础计算测试 ===")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"4 × 6 = {multiply(4, 6)}")
    print(f"5! = {factorial(5)}")

    print("\n=== 数论算法测试 ===")
    print(f"17 是否为素数：{is_prime(17)}")
    print(f"48 和 18 的最大公约数：{gcd(48, 18)}")
    print(f"12 和 18 的最小公倍数：{lcm(12, 18)}")
    print(f"100 的质因数分解：{factorize(100)}")