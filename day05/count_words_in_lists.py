def count_words(lst):
    counted_words = set()  # Words we've already counted
    
    for word in lst:
        if word not in counted_words:
            frequency = lst.count(word)
            print(f"'{word}': {frequency}")
            counted_words.add(word)

# Example list of words
words = ["apple", "banana", "Apple", "cherry", "date", "banana", 
            "apple", "elderberry", "fig", "cherry"]

print("Word frequencies:")
count_words(words)
