class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        cursor = self.dictionary
        for c in word:
            if c not in cursor:
                cursor[c] = {}
                cursor["word"] = cursor.get("word", False)
            cursor = cursor[c]
        cursor["word"] = True

    def search(self, word: str) -> bool:
        def search_help(word: str, cursor: dict) -> bool:
            for i, c in enumerate(word):
                if c == '.':
                    if len(cursor) == 0:
                        return False
                    return any(search_help(word[i+1:], cursor[k]) for k in cursor.keys() if k != "word")
                if c not in cursor:
                    return False
                cursor = cursor[c]
            return cursor["word"]

        return search_help(word, self.dictionary)