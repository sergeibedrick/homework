team1_num = 5
formatted_string1 = 'В команде Мастера кода участников: %d !' % team1_num

team2_num = 6
formatted_string2 = 'Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num)

score_2 = 42
formatted_string3 = 'Команда Волшебники данных решила задач: {} !'.format(score_2)

team1_time = 1552.512
formatted_string4 = 'Волшебники данных решили задачи за {} с !'.format(team1_time)

score_1 = 40
formatted_string5 = f'Команды решили {score_1} и {score_2} задач.'

challenge_result = 'Победа команды Волшебники данных!'
formatted_string6 = f'Результат битвы: {challenge_result}'

tasks_total = 82
time_avg = 45.2
formatted_string7 = f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!'

print(formatted_string1)
print(formatted_string2)
print(formatted_string3)
print(formatted_string4)
print(formatted_string5)
print(formatted_string6)
print(formatted_string7)
