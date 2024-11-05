class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        found_words = {}
        word_lower = word.lower()
        for file_name, words in self.all_words.items():
            for index, w in enumerate(words):
                if w.lower() == word_lower:
                    found_words[file_name] = index
                    break
        return found_words

    def count(self, word):
        word_counts = {}
        word_lower = word.lower()
        for file_name, words in self.all_words.items():
            word_counts[file_name] = sum(1 for w in words if w.lower() == word_lower)
        return word_counts


# Пример использования:
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))      # Нахождение слова и его положение в файле
print(finder.count('teXT'))     # Подсчёт количества слов teXT в тексте