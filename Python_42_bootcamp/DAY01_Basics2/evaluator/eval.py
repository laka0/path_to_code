class Evaluator():
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        else:
            eval = 0
            zipped = zip(coefs, words)
            for i in zipped:
                eval += i[0]*len(i[1])          
            return eval

    def enumerate_evaluate(coefs, words):
        pass
