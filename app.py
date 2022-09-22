list_of_strings = ['gabriel', 'natalia', 'chicago']

for name in list_of_strings:
    print(name)


def print_string(name):
    if (name.startswith('g')):
        print("g found", name)


for name in list_of_strings:
    print_string(name)

list_of_users = [
    {
        "username": "gabriel",
        "is_subscribed": True,
        "age": 26
    },
    {
        "username": "natalia",
        "is_subscribed": False,
        "age": 37
    }
]


def filter_users_subscribed(users):
    subscribed_users = []
    for user in users:
        if (user["is_subscribed"] == True):
            subscribed_users.append(user)

    return subscribed_users
