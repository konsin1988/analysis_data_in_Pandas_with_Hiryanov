# import string

# def letter_index(letter: str):
#     letter = letter.lower()
#     assert len(letter) == 1, "Function works only with chars"
#     assert 'a' <= letter <= 'z', "Function works only with chars from 'a' to 'z'"
#     return ord(letter) - ord('a')

# letter_freq = [0] * 26
# with open("orwell_1984.txt") as file:
#     symbol = file.read(1)
#     while symbol:
#         if 'a' <= symbol <= 'z':
#             index = letter_index(symbol)
#             letter_freq[index] += 1
#         symbol = file.read(1)

# sorted_letter_freq = sorted(zip(string.ascii_lowercase, letter_freq), key=lambda pair: pair[1], reverse = True)
# for letter, freq in sorted_letter_freq:
#     print(letter, freq)

from collections import Counter
from string import ascii_lowercase

with open('orwell_1984.txt') as file:
    symbols_freq = Counter(symbol.lower() for line in file for symbol in line if symbol.lower() in ascii_lowercase)

print(*symbols_freq.most_common(), sep='\n')