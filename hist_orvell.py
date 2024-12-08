import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

with open('orwell_1984.txt') as file:
    # words_length_counter = Counter(len(word) for word in file.read().split())
    words_length = [len(word) for word in file.read().split()]
longest_word_length = max(words_length)
plt.hist(words_length, bins=longest_word_length)
# histogram = [words_length_counter[word_length] for word_length in range(1, longest_word_length + 1)]
# plt.hist(np.arange(1, longest_word_length + 1), weights=histogram, bins=longest_word_length )

plt.ylabel("Number of words") 
plt.xlabel("Word's length")
plt.show()

