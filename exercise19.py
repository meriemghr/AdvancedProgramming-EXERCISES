unique_words = set()
total_words = 0  

while True:
    word = input("Enter a word: ").strip().lower()  
    total_words += 1

    if word in unique_words:
        print(f"You typed in {len(unique_words)} unique words.")
        print(f"Total words typed: {total_words}")
        print("Unique words:", sorted(unique_words))

        with open("unique_words.txt", "w") as file:
            for unique_word in sorted(unique_words):
                file.write(unique_word + "\n")
        break
    else:
        unique_words.add(word)
