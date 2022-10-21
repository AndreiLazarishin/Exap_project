import datetime
import logging
import random
import string
from time import sleep


def rand_password(password=13):
    generate_pass = ''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(password)])
    return generate_pass


def rand_email(email=7):
    generate_email = ''.join([random.choice(string.ascii_lowercase) for _ in range(email)]) + '@john.com'
    return generate_email


def rand_username(name=8):
    generate_name = ''.join([random.choice(string.ascii_lowercase) for _ in range(name)])
    return generate_name


def rand_str(stroke=14):
    generate_str = ''.join([random.choice(string.ascii_lowercase) for _ in range(stroke)])
    return generate_str


def wait_until_ok(timeout=5, period=0.5):
    """Reties until OK"""

    log = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):
        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        log.error(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(original_function):
    """Logging actions using docstrings"""
    log = logging.getLogger("[LogDecorator]")

    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        log.info(original_function.__doc__)
        return result

    return wrapper


class User:

    def __init__(self, name='', lastname='', email='', password=''):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    def fill_data(self, name='', lastname='', email='', password=''):
        """Fill user with sample data and values if provided"""
        user = rand_str()
        self.name = f"{user}{rand_username()}" if not name else name
        self.lastname = f"{user}{rand_str()}" if not lastname else lastname
        self.email = f"{user}{rand_email()}" if not email else email
        self.password = f"{user}{rand_password()}" if not password else password


class Post:

    def __init__(self, body=''):
        self.body = body

    def fill_default(self):
        """Fill fields using random data"""
        self.body = rand_str(10)
