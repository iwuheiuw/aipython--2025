import argparse

def unique_words(sentence):
    words = sentence.split()
    return set(words)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", help="The sentence to extract unique words from.", type=str)
    args = parser.parse_args()
    print(unique_words(args.sentence))

if __name__ == "__main__":
    main()
