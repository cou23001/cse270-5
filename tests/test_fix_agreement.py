# test_fix_agreement.py
from build_sentences import fix_agreement

def test_fix_agreement():
    test_cases = [
        # Example 1: Verb is the third word after 'he'
        {
            "original": ['he', 'quickly', 'run', 'to', 'the', 'store'],
            "expected": ['he', 'quickly', 'runs', 'to', 'the', 'store']
        },
        # Example 2: Verb is the third word after 'she'
        {
            "original": ['she', 'eagerly', 'play', 'with', 'the', 'ball'],
            "expected": ['she', 'eagerly', 'plays', 'with', 'the', 'ball']
        },
        # Example 3: Verb is the third word after 'he'
        {
            "original": ['he', 'quickly', 'read', 'the', 'book'],
            "expected": ['he', 'quickly', 'reads', 'the', 'book']
        },
        # Example 4: Verb is the third word after 'she'
        {
            "original": ['she', 'might',  'sing', 'loudly'],
            "expected": ['she', 'might', 'sings', 'loudly']
        }
    ]
    
    for case in test_cases:
        original = case["original"]
        expected = case["expected"]
        
        # Print the original sentence
        print(f"Original Sentence: {original}")
        
        # Apply the fix_agreement function
        fix_agreement(original)
        
        # Print the modified sentence and expected sentence
        print(f"Modified Sentence: {original}")
        print(f"Expected Sentence: {expected}")
        
        # Print whether the test passed
        match = original == expected
        print(f"Match: {match}")
        print("-" * 40)

if __name__ == "__main__":
    test_fix_agreement()
