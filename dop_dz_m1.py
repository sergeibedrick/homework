# исходные ланные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# изиеним тип данных множества и отсортируем по адфовиту
names = sorted(students)
print(names)

# теперь можно написать код (гугл мне в помощь)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
names = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
# создаем словарь
average_grades = {}
for i in range(len(names)):
    average_grades[names[i]] = sum(grades[i]) / len(grades[i])
print(average_grades)

# или так(мне больше нравится:))
average_grades = dict(zip(names, [sum(grade)/len(grade) for grade in grades]))
print(average_grades)