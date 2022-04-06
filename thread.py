import threading
from nltk import ngrams


# Formula di Coefficiente di jaccard
def jaccard_coef(label1, label2):
    return (len(label1.intersection(label2))) / len(label1.union(label2))


# Crea un set di ngrams fatti da 3 lettere
def query_set_maker(query, ngram):
    return set(ngrams(query, ngram))


# Calcolatore del coefficiente di jaccard che è un thread.
# Queta classe trova 3 massimi valori del coefficiente di Jaccard
# in un lessico di parole.
def letters(inputstring):
    return ''.join(filter(str.isalpha, inputstring))


class JaccardCalculator(threading.Thread):
    def __init__(self, thread_id, name, query, linesarray, ngram):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.linesarray = linesarray
        self.ngram = ngram
        self.query = query_set_maker(query, ngram)
        # Array di massimi coefficienti
        self.top3 = [0.0, 0.0, 0.0]
        # Array di parole
        self.similar_words = ["", "", ""]

    def run(self):
        ngramstrings = []
        for element in self.query:
            ngramstrings.append(letters(element))
        dojaccardcalculations = False
        print("Starting " + self.name)
        for line in self.linesarray:
            # Vede se esiste un ngram nella parola di lessico. Altrimenti non fa i calcoli.
            if any(word in line for word in ngramstrings):
                line_set = set(ngrams(line, self.ngram))
                # Calcola il coefficiente jaccard tra query e una parola
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
        print("Exiting " + self.name)
