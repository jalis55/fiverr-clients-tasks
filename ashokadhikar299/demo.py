from ast import pattern
import re
import json


f = open("data.json", "r")
data=json.load(f)
keywords=list(data.keys())



def match(msg):
    if re.search(r"\b(?:" + '|'.join(keywords)   +r")\b", msg['text'].lower()):
        return True
    return False
print(match({"text": "Can some help me what's wrong with the following clojure query?"}))

def handle(msg):
        res=re.match(r"\b(?:" + '|'.join(keywords)   +r")\b", msg['text'].lower())
        if res:
            return (data[res.group(0)])
        return

print(handle({"text": "Can some help me what's wrong with the following splunk query?"}))