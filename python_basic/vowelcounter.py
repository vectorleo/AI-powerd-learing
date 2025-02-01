# this programme takes a word and counts every vowel in it 

word = (input('Enter a word: ')).lower()
word_list = list(word)
vowels = 0

for letter in word_list:
  if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    vowels += 1

print(f'the word {word} has {vowels} vowels.')