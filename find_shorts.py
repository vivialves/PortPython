# Bring the shortest word in sentence
def find_shorts(text):
    text_list = text.split(" ")
    menor = 9999
    l= [len(words)for words in text_list if len(words) < menor]
    return min(l)


print(find_shorts("bitcoin take over the world maybe who knows perhaps"))
