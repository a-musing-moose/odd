def test_can__load_settings(settings):
    assert settings.ROOT_URLCONF == "main.urls"
