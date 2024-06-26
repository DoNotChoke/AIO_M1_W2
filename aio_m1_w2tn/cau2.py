def character_count(word):
    character_statistic = {}
    for c in word:
        if c not in character_statistic:
            character_statistic[c] = 0
        character_statistic[c] += 1
    return character_statistic


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
