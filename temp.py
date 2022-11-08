#Привет, мир!

import math
from math import sqrt


def main():
    number = int(input())
    for k in range(1, 10):
        decompose = to_sum_of_squares(number, k)
        if decompose:
            print(k)
            break


def to_sum_of_squares(n: int, k: 'squares count:int') -> list:
    if (n < 0) or (k <= 0):
        return []
    maximum = round(sqrt(n))
    if n == maximum * maximum:
        return [n]
    for c in range(1, maximum + 1):
        decomposition = to_sum_of_squares((n - c * c), k - 1)
        if decomposition:
            return [c * c] + decomposition


if __name__ == '__main__':
    main()


def main(N):
    sqrt = int(math.sqrt(N))
    if N == sqrt * sqrt:
        return [N]
    res = []
    Y = x = math.ceil(math.sqrt(N) / 2)
    x_sq = x * x
    while x_sq <= N:
        while Y and (Y - 1) * (Y - 1) * 3 >= N - x_sq:
            Y -= 1
        y = Z = Y
        y_sq = y * y
        while (y <= x) and (x_sq + y_sq <= N):
            while Z and (Z - 1) * (Z - 1) * 2 >= N - x_sq - y_sq:
                Z -= 1
            z = t = Z
            z_sq = z * z
            while (z <= y) and (x_sq + y_sq + z_sq <= N):
                while t * t > N - x_sq - y_sq - z_sq:
                    t -= 1
                if x_sq + y_sq + z_sq + t * t == N:
                    r = [x_sq, y_sq, z_sq, t * t]
                    res.append(r)
                z += 1
                z_sq = z * z
            y += 1
            y_sq = y * y
        x += 1
        x_sq = x * x

    for r in res:
        while 0 in r:
            r.remove(0)
    res.sort(key=lambda x: len(x))
    return res[0]