# Скопировать из файла F1 в файл F2 строки, начиная с четвертой по порядку.
file = open('textfile.txt')
new_file = open('new_text_file.txt', 'a')
n = 0
for row in file:
    n += 1
ammout_of_lines = []

for i in range(4, n + 1):
    ammout_of_lines.append(i)

for num, line in enumerate(file):
    if num in ammout_of_lines:
        new_file.write(line)

file.close()
new_file.close()
