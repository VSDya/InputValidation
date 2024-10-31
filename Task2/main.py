# Вам нужно сделать валидацию входных данных (Input validation) и санитизацию выходных данных 
# (Sanitize) в команды к операционной системе при создании каталогов для хранения материалов заявокзаказов

#Input validation + Output encoding (sanitization)
# import os
# input_path = input('Catalogue path:')
# command = f'mkdir {input_path}'
# os.popen(command)

# Catalogue path:C:\\_WORK\\test1 & %windir%\\system32\\notepad.exe
# Таким образом можно запустить вредоносную программу

# (Ответ с проверкой на вводимые символы)
import os
input_path = input('Catalogue path:')
spec_symbols = ['*', '?', '<', '>', '|', '&']
check = [characters in input_path for characters in spec_symbols]
while True in check:
    for i in range(len(check)):
        check[i] = False
    print('Incorrect Catalogue path')
    input_path = input('Catalogue path:')
    check = [characters in input_path for characters in spec_symbols]
command = f'mkdir {input_path}'
os.popen(command)
print('Catalogue was successfully created')
