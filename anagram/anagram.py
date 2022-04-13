def find_anagrams(word, candidates):
    #pass
    new_word = [[char for char in w if char in word]for w in candidates if len(w) == len(word)]
    return new_word
    # for w in candidates:
    #     if len(w) == len(word):
    #         for char in w:


print(find_anagrams("master",["stream", "pigeon", "maters"]))