def get_message(key, lang="uz"):
    messages = {
        "welcome": {
            "uz": "Xush kelibsiz!",
            "en": "Welcome!",
            "ru": "Добро пожаловать!"
        }
    }
    return messages.get(key, {}).get(lang, key)