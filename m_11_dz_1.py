# Requests - это мощная библиотека для работы с HTTP-запросами.
import requests

# GET-запрос
response = requests.get('https://api.example.com/users')
print(f"Код состояния: {response.status_code}")
print(f"Данные: {response.json()}")

# POST-запрос
data = {'name': 'John', 'age': 30}
response = requests.post('https://api.example.com/users', data=data)
print(f"Код состояния: {response.status_code}")
print(f"Ответ сервера: {response.json()}")

# Работа с параметрами запроса
params = {'page': 1, 'limit': 10}
response = requests.get('https://api.example.com/users', params=params)
print(f"URL с параметрами: {response.url}")
print(f"Данные: {response.json()}")



# Pillow - это библиотека для обработки изображений.
from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('input.jpg')

# Изменение размера
resized_image = image.resize((300, 200))
resized_image.save('resized.jpg')

# Применение фильтра
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred.jpg')

# Поворот изображения
rotated_image = image.rotate(45)
rotated_image.save('rotated.jpg')

# Конвертация в другой формат
image.save('output.png')




# NumPy для работы с многомерными массивами и математическими функциями.
import numpy as np

# Создание массивов
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.arange(0, 10, 2)  # создает массив [0, 2, 4, 6, 8]
arr3 = np.zeros((3, 3))  # создает матрицу 3x3 из нулей

print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:\n", arr3)

# Математические операции
sum_arr = arr1 + arr2
product_arr = arr1 * arr2
sqrt_arr = np.sqrt(arr1)

print("Сумма arr1 и arr2:", sum_arr)
print("Произведение arr1 и arr2:", product_arr)
print("Квадратный корень из arr1:", sqrt_arr)

# Статистические функции
mean = np.mean(arr1)
median = np.median(arr1)
std_dev = np.std(arr1)

print("Среднее значение arr1:", mean)
print("Медиана arr1:", median)
print("Стандартное отклонение arr1:", std_dev)

# Работа с матрицами
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

matrix_product = np.dot(matrix1, matrix2)
matrix_transpose = matrix1.T

print("Произведение матриц:\n", matrix_product)
print("Транспонированная matrix1:\n", matrix_transpose)
