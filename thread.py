import threading
from nltk import ngrams


def jaccard_coef(label1, label2):
    return (len(label1.intersection(label2))) / len(label1.union(label2))


def query_set_maker(query):
    return set(ngrams(query, 3))


class JaccardCalculator(threading.Thread):
    def __init__(self, thread_id, name, query, lexicon):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.lexicon = lexicon
        self.query = query_set_maker(query)
        self.top3 = [0.0, 0.0, 0.0]
        self.similar_words = ["", "", ""]

    def run(self):
        print("Starting " + self.name)
        f = open(self.lexicon, "r")
        while True:
            line = f.readline()
            if not line:
                break
            else:
                line = line.rstrip("\n")
                line_set = set(ngrams(line, 3))
                jc = jaccard_coef(self.query, line_set)
                if jc > self.top3[0]:
                    self.top3[0] = jc
                    self.similar_words[0] = line
                elif jc > self.top3[1]:
                    self.top3[1] = jc
                    self.similar_words[1] = line
                elif jc > self.top3[2]:
                    self.top3[2] = jc
                    self.similar_words[2] = line
        f.close()
        print("Exiting " + self.name)
