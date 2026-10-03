def match_word(words):
    lst = []
    crc = 0
    for word in words:
        crc += 1
        lst.append(word)
    print("List with words that starts and ends with the same letter",lst)
    return crc
count = match_word(["gyvg","drtv","srzfty"])
print("words that start and end with the same letter", count)