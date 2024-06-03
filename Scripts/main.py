from principals.first_substring import first_substr
from testS.test_first_substring import test_normal_case, test_less_than_two_characters_left, test_character_not_in_word, test_word_is_empty, test_char_is_empty, test_word_and_char_are_empty, test_word_is_less_than_three_characters


def main():
    test_normal_case()
    test_less_than_two_characters_left()
    test_character_not_in_word()
    test_word_is_empty()
    test_char_is_empty()
    test_word_and_char_are_empty()
    test_word_is_less_than_three_characters()

    print('All tests passed')

if __name__ == '__main__':
    main()