def test_get_word():
    # Test cases with uppercase letters and out-of-range indices
    test_cases = [
        ('A', ["quick", "lazy"], "quick"),  # A -> index 0
        ('B', ["quick", "lazy"], "lazy"),   # B -> index 1
        ('C', ["quick", "lazy"], None),     # C -> index 2 (out of range)
        ('D', ["quick", "lazy"], None),     # D -> index 3 (out of range)
        ('A', ["cat", "dog", "fish"], "cat"),  # A -> index 0, with more elements
        ('C', ["cat", "dog", "fish"], "fish"),  # C -> index 2, valid for this list
        ('F', ["cat", "dog", "fish"], None)   # F -> index 5 (out of range), with more elements
    ]

    for letter, speech_part, expected in test_cases:
        result = get_word(letter, speech_part)
        result_message = result if result is not None else "out of range"
        print(f"Letter: {letter}, Result: {result_message}, Expected: {expected}")

if __name__ == '__main__':
    test_get_word()
