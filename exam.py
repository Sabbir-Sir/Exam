def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    v = ["a", "e", "i", "o", "u"]
    count = 0
    for i in text.lower():
        if i in v:
            count += 1
    return count

def word_count(text):
    return len(text.split())

if __name__ == "__main__":
    print(reverse_string("Hello"))
    print(count_vowels("hello"))
    print(word_count("helloo"))