import random
input_text = open(input("input file name: ") + '.txt', encoding='utf8').read()
input_list = input_text.split()
def make_pairs(oplist):
    for x in range(len(oplist) - 1):
        yield (oplist[x], oplist[x + 1])
pairs = make_pairs(input_list)
word_dict = {}
for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
first_word = random.choice(input_list)
chain = [first_word]
n_words = int(input("string length: "))
for x in range(n_words):
    chain.append(random.choice(word_dict[chain[-1]]))
print(' '.join(chain))