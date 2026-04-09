import secrets
import string

storage = {} # Хранилище в памяти

def shorten_url(long_url: str) -> str:
    """Генерирует короткий код и сохраняет URL."""
    letters = string.ascii_lowercase + string.digits
    while True:
        short_code = ''.join(secrets.choice(letters) for _ in range(6))
        
        if short_code not in storage:
            storage[short_code] = long_url
            return short_code

def get_original_url(short_code: str) -> str | None:
    """Возвращает оригинальный URL по короткому коду."""
    return storage.get(short_code)