file_path = 'P1_data.txt'


def count_word(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    word_counts = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower().strip()
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

    sorted_dict = dict(sorted(word_counts.items()))
    return sorted_dict


word_dict = count_word(file_path)
print(word_dict)
