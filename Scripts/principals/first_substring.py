def first_substr(word, char):
    index = word.find(char)
    if index == -1 or index > len(word) - 3:
        return None
    else:
        return word[index:index+3]