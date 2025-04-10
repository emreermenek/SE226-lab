from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length

def main():
    s = input("Enter a sentence: ")
    print("Reversed:", reverse_string(s))
    print("Capitalized:", capitalize_words(s))
    no_punct = remove_punctuation(s)
    print("Without punctuation:", no_punct)
    print("Character count:", count_characters(no_punct))
    print("Word count:", count_words(no_punct))
    print("Average word length:", average_word_length(no_punct))

if __name__ == "__main__":
    main()
