numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Исходный код:\n numbers =", numbers)
primes = []
not_primes = []

# Перебираем список чисел
for num in numbers:
    if num == 1:
        continue
    is_prime = True # Предполагаем, что число простое
    for i in range(2, int(num ** 0.5) + 1):  # Проверяем делители до квадратного корня числа
            if num % i == 0:
                is_prime = False  # Если нашли делитель, число не простое
                break

    if is_prime:
        primes.append(num)  # Добавляем в список простых чисел
    else:
        not_primes.append(num)  # Добавляем в список не простых чисел

print("Вывод на консоль:")
print("Primes:", primes)
print("Not Primes:", not_primes)

