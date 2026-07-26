def word_frequency(text):

    text = text.lower()

    text = text.replace(".", "")
    text = text.replace(",", "")

    words = text.split()

    count = {}

    for word in words:

        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    word_list = list(count.items())

    word_list.sort(key=lambda x: x[1], reverse=True)

    return word_list[:3]


text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world.
Many tourists visit Nepal every year to see Everest
and other mountains. Nepal is known for its
mountains and natural beauty.
"""

top_words = word_frequency(text)

print("Top 3 words:")

for word, times in top_words:
    print(word, "-", times, "times")