import numpy as np
from scipy.stats import mannwhitneyu


def test_nd_nd(loc1: float, scale1: float, loc2: float, scale2: float, cnt: int, alpha: float):
    selection1 = np.random.normal(loc1, scale1, cnt)
    selection2 = np.random.normal(loc2, scale2, cnt)
    print("Первая выборка (" + str(loc1) + ", " + str(scale1) + ")")
    print(selection1)
    print("Вторая выборка (" + str(loc2) + ", " + str(scale2) + ")")
    print(selection2)
    stat, p = mannwhitneyu(selection1, selection2)
    print("Статистика: " + str(stat))
    print("p-значение: " + str(p))
    if p > alpha:
        print("Однородны")
    else:
        print("Неоднородны")


def test_nd_ud(loc: float, scale: float, a: float, b: float, cnt: int, alpha: float):
    selection1 = np.random.normal(loc, scale, cnt)
    selection2 = (np.random.rand(cnt) * (b - a)) + a
    print("Первая выборка (" + str(loc) + ", " + str(scale) + ")")
    print(selection1)
    print("Вторая выборка (" + str(a) + ", " + str(b) + ")")
    print(selection2)
    stat, p = mannwhitneyu(selection1, selection2)
    print("Статистика: " + str(stat))
    print("p-значение: " + str(p))
    if p > alpha:
        print("Однородны")
    else:
        print("Неоднородны")


def test_ud_ud(a1: float, b1: float, a2: float, b2: float, cnt: int, alpha: float):
    selection1 = (np.random.rand(cnt) * (b1 - a1)) + a1
    selection2 = (np.random.rand(cnt) * (b2 - a2)) + a2
    print("Первая выборка (" + str(a1) + ", " + str(b1) + ")")
    print(selection1)
    print("Вторая выборка (" + str(a2) + ", " + str(b2) + ")")
    print(selection2)
    stat, p = mannwhitneyu(selection1, selection2)
    print("Статистика: " + str(stat))
    print("p-значение: " + str(p))
    if p > alpha:
        print("Однородны")
    else:
        print("Неоднородны")


def main():
    test_nd_nd(0, 1, 0, 2, 30, 0.05)
    print()
    print()
    test_nd_ud(0, 1, -1, 1, 30, 0.05)
    print()
    print()
    test_ud_ud(-2, 2, -2.5, 2.5, 30, 0.05)


if __name__ == "__main__":
    main()
