'''
lala
'''


class Evaluator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        if len(words) != len(coefs):
            return -1
        return sum([len(item[0]) * item[1] for item in list(zip(words, coefs))])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list):
            return -1
        if len(words) != len(coefs):
            return -1
        sum = 0
        for count, w in enumerate(words):
            sum += len(w) * coefs[count]
        return sum
