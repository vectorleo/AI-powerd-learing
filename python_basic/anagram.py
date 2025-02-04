# this program checkes two word to see if the are Anagrams 

def anagram_checker(word1=str,word2=str):
  wordlist1 = list(word1.lower())
  wordlist2 = list(word2.lower())

  wordlist1.sort()
  wordlist2.sort()

  if wordlist1 == wordlist2:
    return True
  else:
    return False


print(anagram_checker("Listen","Silent"))
print(anagram_checker("Hello","World"))