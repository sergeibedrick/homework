def custom_write(file_name : str, strings  : list) -> dict:
    string_position = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            position = file.tell()
            file.write(string + '\n')
            string_position[i, position] = string
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)