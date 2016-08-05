"""
Word Filter
-----------

Print out only words that start with "s"::

    speech = '''We shall fight on the beaches,
                we shall fight on the landing grounds,
                we shall fight in the fields and in the streets,
                we shall fight in the hills;
                we shall never surrender...
             '''

Bonus points: print out words only once.
"""
speech = '''We shall fight on the beaches,
            we shall fight on the landing grounds,
            we shall fight in the fields and in the streets,
            we shall fight in the hills;
            we shall never surrender...
         '''

# Convert to lower case so case is ignored in comparison.
# Replace punctuation, and split the words into a list.
words = speech.lower().replace('.','').replace(',','').replace(';','').split()

#import string
# Alternate (all punctuation):
#words = speech.lower().translate(None, string.punctuation).split()

# Make a set and fill it with 's' words:
s_words = set(word for word in words if word.startswith('s'))

print "unique set of words that start with 's':"
print s_words
