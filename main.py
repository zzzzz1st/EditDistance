from thread import JaccardCalculator
from edit_distance import editDistDP
import time
start_time = time.time()
query = "andiamo"
coef = [0, 0, 0]
words = ["", "", ""]
distance = [0, 0, 0]
threads = [JaccardCalculator("thread_1", "th1", query, "660000_parole_italiane_1.txt"),
           JaccardCalculator("thread_2", "th2", query, "660000_parole_italiane_2.txt"),
           JaccardCalculator("thread_3", "th3", query, "660000_parole_italiane_3.txt"),
           JaccardCalculator("thread_4", "th4", query, "660000_parole_italiane_4.txt"),
           JaccardCalculator("thread_5", "th5", query, "660000_parole_italiane_5.txt"),
           JaccardCalculator("thread_6", "th6", query, "660000_parole_italiane_6.txt")]
threads[0].start()
threads[1].start()
threads[2].start()
threads[3].start()
threads[4].start()
threads[5].start()
threads[0].join()
threads[1].join()
threads[2].join()
threads[3].join()
threads[4].join()
threads[5].join()
all_coef = list(threads[0].top3)
all_coef.extend(threads[1].top3)
all_coef.extend(threads[2].top3)
all_coef.extend(threads[3].top3)
all_coef.extend(threads[4].top3)
all_coef.extend(threads[5].top3)
maximum = max(all_coef)
coef[0] = maximum
words[0] = threads[int(all_coef.index(maximum) / 3)].similar_words[all_coef.index(maximum) % 3]
all_coef[all_coef.index(maximum)] = 0
maximum = max(all_coef)
coef[1] = maximum
words[1] = threads[int(all_coef.index(maximum) / 3)].similar_words[all_coef.index(maximum) % 3]
all_coef[all_coef.index(maximum)] = 0
maximum = max(all_coef)
coef[2] = maximum
words[2] = threads[int(all_coef.index(maximum) / 3)].similar_words[all_coef.index(maximum) % 3]
all_coef[all_coef.index(maximum)] = 0
distance[0] = editDistDP(query, words[0], len(query), len(words[0]))
distance[1] = editDistDP(query, words[1], len(query), len(words[1]))
distance[2] = editDistDP(query, words[2], len(query), len(words[2]))
spent_time = time.time() - start_time
print(f'''

        Calculations Done !!


        Word : {words[0]} 
        with Jaccard Coefficient : --- {coef[0]} --- has the minimum distance : {distance[0]}
      
        Word : {words[1]} 
        with Jaccard Coefficient : --- {coef[1]} --- has the distance : {distance[1]}

        Word : {words[2]} 
        with Jaccard Coefficient : --- {coef[2]} --- has the distance : {distance[2]}

        Spent time : {spent_time} seconds ! ''')
