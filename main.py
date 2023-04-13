def is_vald_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False
side1, side2, side3 = int(input()), int(input()), int(input())
print(is_vald_triangle(side1, side2, side3))