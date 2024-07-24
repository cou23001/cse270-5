import pytest
import json

from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word():
    # Mock input to return a 7-letter word
    mock_res = mocker.patch('builtins.input', mock_input)
    
    assert get_seven_letter_word() == "EXAMPLEWORD"
    