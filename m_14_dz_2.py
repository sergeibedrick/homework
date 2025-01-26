import sqlite3

# Создаем файл базы данных not_telegram.db и подключаемся к ней
conn = sqlite3.connect('not_telegram_dz_14_2.db')
cursor = conn.cursor()

# Создаем таблицу Users с указанными полями, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')
conn.commit()

# Заполняем таблицу Users 10 записями с указанными данными
users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users)


# Обновляем balance у каждой 2-й записи начиная с 1-й
cursor.execute("UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1")


# Удаляем каждую 3-ю запись начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")


# Делаем выборку всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()

# Удаляем из базы данных запись с id = 6.
cursor.execute("DELETE FROM Users WHERE id = 6")


# Подсчитываем общее количество записей.
cursor.execute('SELECT COUNT(*) FROM users')
total_records = cursor.fetchone()[0]

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM users')
total_balance = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователей.
if total_records > 0:
    average_balance = total_balance / total_records
else:
    average_balance = 0

print(f'Средний баланс всех пользователей: {average_balance}')

# Выводим результаты в консоль в указанном формате
for row in results:
    username, email, age, balance = row
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# Закрываем соединение
conn.commit()
conn.close()