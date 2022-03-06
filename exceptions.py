class TranslationException(Exception):
    """Exception raised for unknown translation key.

    Attributes:
        key -- input translation key which caused the error
        message -- explanation of the error
    """
    def __init__(self, key, message="Translation key does not exist in data"):
        self.key = key
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.key} -> {self.message}'