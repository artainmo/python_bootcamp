class Evaluator:

    def zip_evaluate(coefs, words):
        x = 0
        tot = 0
        if len(coefs) != len(words):
            return -1
        zipped = zip(coefs, words)
        for tuple in zipped:
            x = tuple[0] * len(tuple[1])
            tot += x
        return tot

    def enumerate_evaluate(coefs, words):
        x = 0
        tot = 0
        if len(coefs) != len(words):
            return -1
        enum_c = list(enumerate(coefs))
        enum_w = list(enumerate(words))
        for i in range(0, len(coefs)):
                x = enum_c[i][1] * len(enum_w[i][1])
                tot += x
        return tot

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.enumerate_evaluate(coefs, words))
print(Evaluator.zip_evaluate(coefs, words))
