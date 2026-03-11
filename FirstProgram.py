import string

text = input("Enter a sentence: ")
text = text.lower()

clean_text = ""

for ch in text:
    if ch not in string.punctuation:
        clean_text += ch

words = clean_text.split()

stopwords = ["is","and","the","a","an"]

filtered = []

for w in words:
    if w not in stopwords:
        filtered.append(w)

freq = {}

for w in filtered:
    freq[w] = freq.get(w,0) + 1

print("Clean words:", filtered)
print("Word frequency:", freq)