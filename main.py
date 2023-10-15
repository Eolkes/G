#1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Введите число: "))
if is_prime(num):
    print(num +"простое число")
else:
    print(num + "не простое число")
#2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 2, 9, 3, 8, 6]
bubble_sort(arr)
print("Отсортированный массив:", arr)
#3
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [5, 2, 9, 3, 8, 6]
max_element = find_max(arr)
print("Наибольший элемент в массиве:", max_element)
#4
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Введите номер числа Фибоначчи: "))
result = fibonacci(num)
print("Число Фибоначчи под номером {num} равно {result}")
#5
def most_common_string(strings):
    counts = {}
    most_common = ""
    max_count = 0

    for string in strings:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1

        if counts[string] > max_count:
            max_count = counts[string]
            most_common = string

    return most_common

str = ["apple", "banana", "apple", "cherry", "banana"]
result = most_common_string(str)
print("Наиболее часто встречающаяся строка:", result)