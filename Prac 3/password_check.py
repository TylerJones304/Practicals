def main():
    password = get_password()
    display_pass(password)


def password(args):
    pass


def display_pass():
    print('*' * len(password))


def get_password():
    password = input("Enter password with at least 4 characters: ")
    while len(password) < 4:
        print("Invalid password")
        password = input("Enter password with at least 4 characters: ")
    return password


main()
