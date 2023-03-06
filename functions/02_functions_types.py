# 1 - Performs a task
# 2 - Return a value


print('Hello')
round(9.8)  # Returns a rounded value which is passed as an arguments


def greet_user(name):
    return f'Hello, {name}'


message = greet_user('Ammu')
file = open('content.txt', 'w')
file.write(message)
file.close
