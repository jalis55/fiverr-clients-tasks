import re
def match(msg):
    if re.search(r"\b(?:spark|splunk |Clojure )\b", msg['text'].lower()):
        return True
    return False
    

# match({"text": "Can some help me what's wrong with the following splunk query?"})

def handle(msg):
    if re.search(r"\b(?:splunk)\b", msg['text'].lower()):
        return "@PersonA to see if he can help this Splunk question"
    if re.search(r"\b(?:spark)\b", msg['text'].lower()):
        return "@PersonB to see if she can help this Spark question"
    if re.search(r"\b(?:clojure )\b", msg['text'].lower()):
        return "@PersonC to see if she can help this Clojure  question"
    
print(handle({"text": "Question on the following Clojure query"}))
