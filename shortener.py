import random
import string

storage = {} # Хранилище в памяти

def shorten_url(long_url: str) -> str:
    """Генерирует короткий код и сохраняет URL."""
    letters = string.ascii_lowercase + string.digits
    short_code = ''.join(random.choice(letters) for i in range(6))
    storage[short_code] = long_url
    return short_code

def get_original_url(short_code: str) -> str | None:
    """Возвращает оригинальный URL по короткому коду."""
    return storage.get(short_code)