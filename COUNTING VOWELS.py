# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

word = str(raw_input("Enter a word: "));
numVowel = 0
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        numVowel += 1
print("Number of vowels: " + str(numVowel))
