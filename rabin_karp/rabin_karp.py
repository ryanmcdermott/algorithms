class RollingHash:
    def __init__(self, text, pattern_size):
        self.text = text
        self.pattern_size = pattern_size
        self.hash = RollingHash.hash_text(text, pattern_size)
        self.start = 0
        self.end = pattern_size
        self.alphabet = 26

    def move_window(self):
        if self.end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.start]) -
                          ord("a") + 1) * self.alphabet ** (self.pattern_size - 1)
            self.hash *= self.alphabet
            self.hash += ord(self.text[self.end]) - ord("a") + 1
            self.start += 1
            self.end += 1

    def get_text_window(self):
        return self.text[self.start:self.end]

    @staticmethod
    def hash_text(text, limit, hash=0, alphabet=26):
        h = hash
        for i in range(0, limit):
            h += (ord(text[i]) - ord("a") + 1) * \
                (alphabet ** (limit - i - 1))

        return h


def rabin_karp(pattern, text):
    res = []

    if pattern == "" or text == "" or len(pattern) > len(text):
        return res

    pattern_hash = RollingHash.hash_text(pattern, len(pattern))
    text_hash = RollingHash(text, len(pattern))

    for i in range(0, len(text) - len(pattern) + 1):
        if text_hash.hash == pattern_hash and text_hash.get_text_window() == pattern:
            res.append(i)

        text_hash.move_window()

    return res
