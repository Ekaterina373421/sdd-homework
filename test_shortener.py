from shortener import shorten_url, get_original_url, storage

def test_shorten_and_get():
    """Тест полного цикла: сократить и получить обратно."""
    storage.clear()
    long_url = "https://very-long-and-complex-url.com/page1"
    short_code = shorten_url(long_url)
    assert get_original_url(short_code) == long_url

def test_get_nonexistent():
    """Тест получения несуществующего URL."""
    storage.clear()
    assert get_original_url("nonexist") is None

def test_storage_has_value():
    """Тест, что URL добавляется в хранилище."""
    storage.clear()
    long_url = "https://google.com"
    short_code = shorten_url(long_url)
    assert storage[short_code] == long_url