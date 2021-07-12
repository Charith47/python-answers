# Paragraph has these properties:
#   Paragraph content (length > 2 sentences)

# This class has following methods:
#   get_words() -> returns the set of words in the para
#   get_sentences() -> returns the list of sentences
#   get_word_count() -> returns the word count
#   get_sentence_count() -> returns the sentence count
#   get_length_distribution()
import re


class Paragraph:
    def __init__(self, text):
        self.__text = text

    def get_words(self):
        return set(self.__getcleanstring().split())

    def get_sentences(self):
        return list(filter(None, self.__text.split(".")))

    def get_word_count(self):
        return len(self.__getcleanstring().split())

    def get_sentence_count(self):
        return len(self.get_sentences())

    def __getcleanstring(self):
        return re.sub("[^\w\s]", "", self.__text).lower()

    def get_distribution_data(self):
        data = []

        word_list = list(self.get_words())
        word_lengths = sorted(set(map(len, word_list)))

        min_length = word_lengths[0]
        max_length = word_lengths[len(word_lengths) - 1]

        for length in word_lengths:
            count = 0
            datum = dict({length: count})
            for word in word_list:
                if len(word) == length:
                    datum[length] = datum.get(length, 0) + 1
            data.append(datum)

        return {
            "data": data,
            "min_len": min_length,
            "max_len": max_length,
        }


def print_distribution(info):
    data = info.get("data")
    start = info.get("min_len")
    end = info.get("max_len")

    print("LENGTH | COUNT")
    for length in range(start, end + 1):
        count = 0
        for value in data:
            if value.get(length):
                count = value.get(length)
                break
        print(f"[{str(length).zfill(2)}]", end=" ")
        for i in range(1, count + 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    paragraph_string = "Lorizzle dolor sit shizzlin dizzle, own yo' adipiscing elit. Nullizzle fo shizzle my nizzle velizzle, gizzle volutpizzle, suscipit quizzle, rizzle vizzle, arcu. Phat egizzle tortizzle. Sizzle eros. Get down get down fo shizzle dolor dapibizzle turpis tempizzle tempizzle. Mauris pellentesque nibh et turpizzle. Vestibulum izzle . Boofron rhoncizzle nisi. In gangsta get down get down fizzle dictumst. Shut the shizzle up owned. Break yo neck, yall tellus break it down, pretizzle eu, mattis izzle, ass vitae, nunc. Dizzle suscipit. Integer fo shizzle velit sed hizzle."
    sample = Paragraph(paragraph_string)
    print_distribution(sample.get_distribution_data())
