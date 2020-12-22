data_base = {
    "Varya": "helloworld",
    "GVarya": "iloveyou"
}




def check_password(login, password):
    if login in data_base:
        if data_base[login] == password:
            return True
        return False
    #
    #     else:
    #         return"неверный пароль"
    # else:
    #     return"вас нет в системе"



user_login = "GVarya"
count = 0
passwords = ["1", "2", 'dfs', 'ggg']

with open("pop-passwords.txt") as passwords_file:
    for line in passwords_file:
        user_password = line.strip()
        if check_password(user_login, user_password) == True:
            print(f"попытка №{count} пароль подошёл")
            break
        else:
            count+=1



# for password in passwords:
#     print(password)
#     print(check_password(user_login, password))