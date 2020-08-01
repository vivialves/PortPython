from collections import Counter

def duplicate_count(text):
    # Return the count of distinct case-insensitive alphabetic characters
    text_lower = text.lower()
    letters = [letter for letter in text_lower]
    count = Counter(letters)
    lists = count.most_common(len(letters))
    print(lists)
    quant = [lists[i][1] for i in range(0, len(lists)) if lists[i][1] != 1]
    return len(quant)


print(duplicate_count("Suuaaas"))