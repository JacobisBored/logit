"""
Word Sort
---------

Given a some lytics from a song, print the words found in the
sentence in alphabetical order.  Also print out just the first
three words and the last three words in the sorted list.

    lyrics = '''Humpty Dumpty sat on the wall,
                Humpty Dumpty had a great fall.
                All the king's horses
                and all the king's men
                couldn't put Humpty Dumpty
                together again.
             '''

Remove all punctuation, and sort ignoring case.
"""
lyrics = '''Humpty Dumpty sat on the wall,
            Humpty Dumpty had a great fall.
            All the king's horses
            and all the king's men
            couldn't put Humpty Dumpty
            together again.
         '''

# Convert to lower case so case is ignored in sorting.
# Replace punctuation, and split the words into a list.
# Then sort in place:
#words = lyrics.lower().replace('.', '').replace(',', '').split()
#words.sort()

import string
# Alternate (all punctuation):
words = lyrics.lower().translate(None, string.punctuation).split()
words.sort()

# Alternate (preserving case):
#words = lyrics.translate(None, string.punctuation).split()
#words.sort(key=string.lower)

print "All words, in alphabetical order:"
print words
print
print "The first 3 words: "
print words[:3]
print
print "The last 3 words: "
print words[-3:]
