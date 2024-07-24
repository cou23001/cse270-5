import pytest
import json
import random
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value="example")
    assert get_seven_letter_word() == "EXAMPLE"
    
def test_get_seven_letter_word_invalid_input(mocker):
    mocker.patch('builtins.input', return_value='cat')
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file(mocker):
    mock_data = {"adjectives": ["quick", "lazy"], "nouns": ["fox", "dog"], "verbs": ["jumps", "runs"], "adverbs": ["quickly", "slowly"], "prepositions": ["over", "under"]}
    mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(mock_data)))
    result = parse_json_from_file("mock_path")
    assert result == mock_data

def test_choose_sentence_structure():
    # Test if the function returns a valid structure
    structure = choose_sentence_structure()
    assert structure in structures

def test_get_pronoun():
    # Test if the function returns a valid pronoun
    pronoun = get_pronoun()
    assert pronoun in ["he", "she", "they", "I", "we"]

def test_get_article():
    # Test if the function returns a valid article
    article = get_article()
    assert article in ["a", "the"]

def test_get_word():
    # Test with a fixed letter and mock data
    mock_data = {"adjectives": ["quick"], "nouns": ["fox"], "verbs": ["jumps"], "adverbs": ["quickly"], "prepositions": ["over"]}
    assert get_word('A', mock_data["nouns"]) == "fox" 

def test_fix_agreement_he_she_rule():
    sentence = ["he", "always", "run"]
    fix_agreement(sentence)
    assert sentence == ["he", "always", "runs"]

def test_fix_agreement_a_to_an_rule():
    sentence = ["I", "saw", "a", "apple","avalanche"]
    fix_agreement(sentence)
    assert sentence == ["I", "saw", "an", "apple", "avalanche"]
    
def test_fix_agreement_the_rule():
    sentence = ["the", "cat", "will", "chase", "mouse"]
    fix_agreement(sentence)
    assert sentence == ["the", "cat", "will", "chase", "mouses"]
    
    sentence = ["the", "dog", "might", "bite", "boy"]
    fix_agreement(sentence)
    assert sentence == ["the", "dog", "might", "bite", "boys"]

def test_build_sentence(mocker):
    mock_data = {
        "adjectives": ["quick", "lazy", "bright"],
        "nouns": ["fox", "dog", "cat"],
        "verbs": ["jump", "sleep", "run"],
        "adverbs": ["quickly", "slowly"],
        "prepositions": ["to", "at", "by"],
    }

    seed_word = "BCAAAAAAAAAAAAAA"  

    sentence = build_sentence(seed_word, structures[1], mock_data)

    expected_sentence = [
        "He slowly runs the quick fox to the quick fox",
        "He slowly runs a quick fox to the quick fox",
        "He slowly runs the quick fox to a quick fox",
        "He slowly runs a quick fox to a quick fox",
        "She slowly runs the quick fox to the quick fox",
        "She slowly runs a quick fox to the quick fox",
        "She slowly runs the quick fox to a quick fox",
        "She slowly runs a quick fox to a quick fox",
        "They slowly run the quick fox to the quick fox",
        "They slowly run a quick fox to the quick fox",
        "They slowly run the quick fox to a quick fox",
        "They slowly run a quick fox to a quick fox",
        "I slowly run the quick fox to the quick fox",
        "I slowly run a quick fox to the quick fox",
        "I slowly run the quick fox to a quick fox",
        "I slowly run a quick fox to a quick fox",
        "We slowly run the quick fox to the quick fox",
        "We slowly run a quick fox to the quick fox",
        "We slowly run the quick fox to a quick fox",
        "We slowly run a quick fox to a quick fox"
    ]

    assert sentence in expected_sentence
