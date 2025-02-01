# this checks if a word is a Palindrome.
word1 = input('enter a word:').lower()
word1_conv = list(word1)

word2_list = word1_conv
word2_list.reverse()
word2 = ''.join(word2_list)

if word1 == word2 :
  print(f'{word1} is a Palindrome.')
else:
  print(f'{word1} is a not Palindrome.')