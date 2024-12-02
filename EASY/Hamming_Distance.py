''' Hamming Distance
Hamming distance is the number of characters that differ between two strings.

To illustrate:

String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.'''


def hamming_distance(txt1, txt2):
 d=0
 for a,b in zip(txt1,txt2):
  if a!=b:
	  d+=1
 return d
	
print(hamming_distance("abcde", "bcdef")) # 5 
print(hamming_distance("abcde", "abcde")) # 0 
print(hamming_distance("strong", "strung")) # 1