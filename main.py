import pandas

phonetics_list = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(phonetics_list)

# TODO 1. Create a dictionary in this format:
phonetics_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        output_list = [phonetics_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Letters in the Alphabet only please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
