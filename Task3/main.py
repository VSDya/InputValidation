# Вам нужно сделать валидацию входных данных (Input validation) для блока с выполнением
# произвольного кода*
# * Необходимость динамического выполнения кода (3 встроенные функции: eval(), exec() и compile())

# Input validation (Arbitrary Code Execution)
# compute_user_input = input('\nFactors and operator for computing: ')
# if not compute_user_input:
#     print ('No input')
# else:
#     print ("Result: ", eval(compute_user_input))

# Ответ(Не использовать функцию evel() для ненадёжного источника ввода)
# Input validation (Arbitrary Code Execution)
compute_user_input = input('\nFactors and operator for computing: ')
if not compute_user_input:
    print('No input')
else:
    print("Result: ", eval(compute_user_input, {'__builtins__':{}}))
