#matching specific words in a string 

import re

sentence=input("Enter input:")

if re.search(r"\b(?:hello|hi|what's up)\b", sentence.lower()):
    print('How are you today!')
