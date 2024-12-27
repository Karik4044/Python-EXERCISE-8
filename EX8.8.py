def count_word_occurrence(input_text):
    word_count = {}
    word_text_split = input_text.split()

    for word in word_text_split:
        word = word.strip(",.")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

input_text = "I chose the red color, because I like red"

result = count_word_occurrence(input_text)
print(result)