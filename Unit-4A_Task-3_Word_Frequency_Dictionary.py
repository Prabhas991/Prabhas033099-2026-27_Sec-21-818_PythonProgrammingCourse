sentence = "apple banana apple mango banana apple"

words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:", frequency)