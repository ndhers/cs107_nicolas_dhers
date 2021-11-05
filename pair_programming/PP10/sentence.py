class Sentence:
    def __init__(self, text): 
        self.words = text.split() 

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == "__main__":
    example = "Rayane is bad at squash"
    sentence = Sentence(example)
    iteration = iter(sentence)
    print(next(iteration))
    print(next(iteration))
    print(next(iteration))
    print(next(iteration))
    print(next(iteration))


