#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 22:18
# @Author : Tptfb11
# @File : wienerHacker.py
# @Software : PyCharm
import gmpy2

def transform(x, y):  # 使用辗转相处将分数 x/y 转为连分数的形式
    res = []
    while y:
        res.append(x // y)
        x, y = y, x % y
    return res

def continued_fraction(sub_res):
    numerator, denominator = 1, 0
    for i in sub_res[::-1]:  # 从sublist的后面往前循环
        denominator, numerator = numerator, i * numerator + denominator
    return denominator, numerator  # 得到渐进分数的分母和分子，并返回

# 求解每个渐进分数
def sub_fraction(x, y):
    res = transform(x, y)
    res = list(map(continued_fraction, (res[0:i] for i in range(1, len(res)))))  # 将连分数的结果逐一截取以求渐进分数
    return res

def get_pq(a, b, c):  # 由p+q和pq的值通过维达定理来求解p和q
    par = gmpy2.isqrt(b * b - 4 * a * c)  # 由上述可得，开根号一定是整数，因为有解
    x1, x2 = (-b + par) // (2 * a), (-b - par) // (2 * a)
    return x1, x2

def wienerAttack(e, n):
    try:
        for (d, k) in sub_fraction(e, n):  # 用一个for循环来注意试探e/n的连续函数的渐进分数，直到找到一个满足条件的渐进分数
            if k == 0:  # 可能会出现连分数的第一个为0的情况，排除
                continue
            if (e * d - 1) % k != 0:  # ed=1 (mod φ(n)) 因此如果找到了d的话，(ed-1)会整除φ(n),也就是存在k使得(e*d-1)//k=φ(n)
                continue

            phi = (e * d - 1) // k  # 这个结果就是 φ(n)
            px, qy = get_pq(1, n - phi + 1, n)
            if px * qy == n:
                p, q = abs(int(px)), abs(int(qy))  # 可能会得到两个负数，负负得正未尝不会出现
                d = gmpy2.invert(e, (p - 1) * (q - 1))  # 求ed=1 (mod  φ(n))的结果，也就是e关于 φ(n)的乘法逆元d
                return d
        return "该方法不适用"
    except:
        return "该方法不适用"

if __name__ == '__main__':
    e = 14058695417015334071588010346586749790539913287499707802938898719199384604316115908373997739604466972535533733290829894940306314501336291780396644520926473
    n = 33608051123287760315508423639768587307044110783252538766412788814888567164438282747809126528707329215122915093543085008547092423658991866313471837522758159
    d = wienerAttack(e, n)
    print(d)