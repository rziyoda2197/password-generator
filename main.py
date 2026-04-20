import string
import secrets

def random_password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(random_password_generator())
```

```python
import string
import secrets

def random_password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(random_password_generator(16))
