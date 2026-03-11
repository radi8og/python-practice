import string

spam_words = ["free", "offer", "win", "money", "prize", "click", "urgent"]

message = input("Enter your message: ")

message = message.lower()

clean_message = ""

for ch in message:
    if ch not in string.punctuation:
        clean_message += ch

words = clean_message.split()

spam_count = 0

for word in words:
    if word in spam_words:
        spam_count += 1
    
if spam_count > 0:
    print("This message is likely to be spam.")
else:    
    print("This message does not appear to be spam.")

print(f"Spam words found: {spam_count}")

