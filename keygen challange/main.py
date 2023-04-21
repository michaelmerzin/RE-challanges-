
def main():
    username = input("enter you're username:\n")
    password = password_getter(username)
    print("you're password is : " + password)


def password_checker(username, password):
    len_user_name = len(username)
    for i in range(0, len_user_name):
        if ord(username[i]) + 3 != ord(password[i]):
            return 0

    return 1


def password_getter(username):
    password = ''
    len_user_name = len(username)
    for i in range(0, len_user_name):
        password += chr(ord(username[i]) + 3)

    return password


if __name__ == '__main__':
    main()
