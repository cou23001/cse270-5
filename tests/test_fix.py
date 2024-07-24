from build_sentences import fix_agreement

def test_fix_agreement_pronoun():
    sentence = ["he", "quickly", "run", "to", "the", "store"]
    print("Before:", sentence)
    fix_agreement(sentence)
    print("After:", sentence)

def test_fix_agreement_article():
    sentence = ["a", "quick", "elephant"]
    print("Before:", sentence)
    fix_agreement(sentence)
    print("After:", sentence)

def test_fix_agreement_the():
    sentence = ["the", "quick", "brown", "fox", "jump", "over", "the", "lazy", "dog"]
    print("Before:", sentence)
    fix_agreement(sentence)
    print("After:", sentence)

def main():
    print("Testing pronoun agreement:")
    test_fix_agreement_pronoun()
    print("\nTesting article agreement:")
    test_fix_agreement_article()
    print("\nTesting 'the' agreement:")
    test_fix_agreement_the()

if __name__ == "__main__":
    main()
