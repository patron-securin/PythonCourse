def find_short_word(s):
  words=s.split()
  short_word = words[0]
  for i in words[1:]:
    if len(i) < len(short_word):
        short_word = i
  print(short_word,';', len(short_word))
