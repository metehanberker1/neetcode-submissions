class PrefixTree:

    def __init__(self):
        self.dictionary = {}

    def insert(self, word: str) -> None:
        cursor = self.dictionary
        for c in word:
            if c not in cursor:
                cursor[c] = {}
                cursor["word"] = cursor.get("word", False) or False
            cursor = cursor[c]
        cursor["word"] = True

    def search(self, word: str) -> bool:
        cursor = self.dictionary
        for c in word:
            if c not in cursor:
                return False
            cursor = cursor[c]
        return cursor["word"]

    def startsWith(self, prefix: str) -> bool:
        cursor = self.dictionary
        for c in prefix:
            if c not in cursor:
                return False
            cursor = cursor[c]
        return True
        