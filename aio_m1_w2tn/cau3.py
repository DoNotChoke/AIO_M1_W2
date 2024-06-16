def count_word(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    counter = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower()
            if word not in counter:
                counter[word] = 0
            counter[word] += 1
    return counter


file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
