class Watch:
    watches_created = 0
    def __init__(self):
        Watch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def engraved_watch(cls, text):
        if cls.test_text(text):
            _watch = cls()
            _watch.text = text
            return _watch

    @staticmethod
    def test_text(text):
        try:
            if len(text) > 40:
                raise ValueError("Text is too long. ")
            if not text.isalnum():
                raise ValueError("Only alphanumerical characters are permitted. ")
            return True
        except ValueError as e:
            print(e)
            return False


print(Watch.watches_created)

watch_1 = Watch()
print(Watch.watches_created)

watch_2 = Watch.engraved_watch("ThisIsAWatch")
print(Watch.watches_created)

watch_3 = Watch.engraved_watch("foo@baz.com")
print(Watch.watches_created)