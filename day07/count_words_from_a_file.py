import sys
import os


def count_words(input_file):
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_counted{ext}"

    # Read input file and count words
    word_counts = {}
    with open(input_file, 'r') as f:
        content = f.read()
        words = content.split()
        for word in words:
            word = word.lower()  # Convert to lowercase
            word_counts[word] = word_counts.get(word, 0) + 1
    
    # Sort words alphabetically
    sorted_words = sorted(word_counts.items())
    
    # Write results to output file
    with open(output_file, 'w') as f:
        max_word_length = max(len(word) for word, _ in sorted_words)
        for word, count in sorted_words:
            f.write(f"{word:<{max_word_length}} {count:>3}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Command line parameter should be the input file name.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    count_words(input_file)
