# pattern = r'.*\b(?='+'|'.join(keywords) + r')\b.*'

import re
keywords=['spark','splunk','clojure']
def match(msg):
    # if re.search(r"\b(?:spark|splunk |Clojure )\b", msg['text'].lower()):
    if re.search(r"\b(?:" +'|'.join(keywords)   +r")\b", msg['text'].lower()):
        return True
    return False
print(match({"text": "Can some help me what's wrong with the following clojure query?"}))