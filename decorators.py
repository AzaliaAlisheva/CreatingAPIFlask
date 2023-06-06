import functools

user = {
    'name': 'Azalia',
    'access_level': 'admin'
}


def secure(*args, **kwargs):
    def decorator (func) :
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user['access_level'] == 'admin':
                return func(*args, **kwargs)
            return 'Access denied'
        return wrapper
    return decorator


@secure('admin')
def get_secure_information(text):
    if text == 'Hello':
        return 'Hello my dear friend!'
    if text == 'Quest':
        return 'How are you?'
    return "Choose between 'Hello' and 'Quest'"


print(get_secure_information('hi'))
