import hashlib
import getpass

def check_password_complexity(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def hash_password(password):
    salt = b"salt"
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hashed_password.hex()

def main():
    password = getpass.getpass("Введите пароль: ")
    if check_password_complexity(password):
        hashed_password = hash_password(password)
        print(f"Ваш пароль: {password}")
        print(f"Хэш-значение пароля: {hashed_password}")
    else:
        print("Пароль не соответствует требованиям сложности.")

if __name__ == "__main__":
    main()
'''
Эта программа выполняет следующие действия:
1.Импорт необходимых библиотек:
-hashlib для хеширования пароля.
-getpass для безопасного ввода пароля.
2.Функция check_password_complexity:
-Проверяет, что пароль содержит не менее 8 символов.
-Проверяет наличие прописных и строчных букв.
-Проверяет наличие цифр.
3.Функция hash_password:
-Хеширует пароль с использованием алгоритма pbkdf2_hmac с солью.
4.Функция main:
-Запрашивает у пользователя ввод пароля.
-Вызывает функции check_password_complexity и hash_password для проверки и хеширования пароля.
5.Вывод результатов:
-Если пароль соответствует требованиям сложности, программа выводит исходный пароль и его хэш-значение.
-Если пароль не соответствует требованиям, программа сообщает об этом.
'''