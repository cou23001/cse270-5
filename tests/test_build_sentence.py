# test_build_sentence.py

import pytest
from build_sentences import build_sentence

# Define mock functions
def mock_get_article():
    return "the"

def mock_get_word(letter, part):
    # Return a mock word based on part
    mock_data = {
        "adjectives": "quick",
        "nouns": "fox",
        "verbs": "jumps",
        "adverbs": "quickly",
        "prepositions": "over"
    }
    return mock_data.get(part, "")

def mock_get_pronoun():
    return "he"

def mock_fix_agreement(sentence):
    # No actual fixing in this mock, just return as-is
    pass

# Test function for build_sentence
def test_build_sentence():
    # Mock data for the test
    mock_data = {
        "adjectives": ["quick"], 
        "nouns": ["fox"], 
        "verbs": ["jumps"], 
        "adverbs": ["quickly"], 
        "prepositions": ["over"]
    }

    # Mock functions for build_sentence
    global get_article, get_word, get_pronoun, fix_agreement
    get_article = mock_get_article
    get_word = mock_get_word
    get_pronoun = mock_get_pronoun
    fix_agreement = mock_fix_agreement

    # Define the seed word and sentence structure for the test
    seed_word = "example"  # This should be at least as long as the number of required letters
    structure = ["ART", "ADJ", "NOUN", "ADV", "VERB", "PREP", "ART", "ADJ", "NOUN"]  # Example structure

    # Build the sentence
    sentence = build_sentence(seed_word, structure, mock_data)

    # Expected result based on the mocks
    expected_sentence = "The quick fox quickly jumps over the quick fox"

    # Print the result and check if it's as expected
    print(f"Generated Sentence: {sentence}")
    assert sentence == expected_sentence, f"Expected '{expected_sentence}', but got '{sentence}'"

if __name__ == '__main__':
    test_build_sentence()
