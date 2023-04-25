# объявление функции
def is_prime(num):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
    if count > 1 or num == 1:
        return False
    else:
        return True

def get_next_prime(num):
    next_num = num + 1
    while is_prime(next_num) is False:
        next_num += 1
    return next_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))