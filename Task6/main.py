# «Authentication and password management»
# Вам нужно безопасно сохранить пароли пользователей (Authentication and password management)

# # «Authentication and password management»
# dict_users = {'user1': 'password1', 'user2': 'passwodr2'}
# print(dict_users)

# Ответ (hashlib или bcrypt)
# «Authentication and password management»
# import hashlib
# dict_users = {'user1': 'password1', 'user2': 'password2'}
# for i in dict_users:
#     dict_users[i] = hashlib.sha256(dict_users[i].encode()).hexdigest()
# print(dict_users)

import bcrypt
dict_users = {'user1': 'password1', 'user2': 'password2'}
for i in dict_users:
    dict_users[i] = bcrypt.hashpw(dict_users[i].encode(),bcrypt.gensalt())
print(dict_users)
