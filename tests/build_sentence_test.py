# build_sentences_test.py
from build_sentences import fix_agreement

def test_fix_agreement():
    # Test cases
    sentences = [
        ["he", "quickly", "run", "to", "the", "store"],
        ["she", "is", "going", "to", "the", "market"],
        ["a", "apple", "is", "on", "the", "table"],
        ["the", "cat", "is", "on", "the", "roof"],
        ["they", "are", "playing", "at", "the", "park"]
    ]

    expected_outputs = [
        ["he", "quickly", "runs", "to", "the", "store"],
        ["she", "is", "going", "to", "the", "market"],
        ["an", "apple", "is", "on", "the", "table"],
        ["the", "cat", "is", "on", "the", "roofs"],
        ["they", "are", "playing", "at", "the", "park"]
    ]

    for sentence, expected in zip(sentences, expected_outputs):
        fix_agreement(sentence)
        print("Modified Sentence:", sentence)
        print("Expected Sentence:", expected)
        print()

if __name__ == '__main__':
    test_fix_agreement()
