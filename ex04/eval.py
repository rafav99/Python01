class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        sum = 0
        for coefs, words in zip(coefs, words):
            sum += len(words) * coefs
        return sum
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        sum = 0
        for index, words in enumerate(words, start=0):
            sum += coefs[index] * len(words)
        return sum
