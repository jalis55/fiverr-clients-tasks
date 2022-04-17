
import whois
import pandas as pd
import time

file=open('domains.txt','r',encoding="mbcs")
domains=file.read().splitlines()
# print(domains[:100])


# domains = [
#     "thepythoncode.com",
#     "google.com",
#     "github.com",
#     "unknownrandomdomain.com",
#     "notregistered.co",
#     "imdb.com",
#     "ztechone.com",
#     "ztes6.com",
#     "zubaisaenterprises.com",
#     "zuendkerzenschluessel.com",
#     "zughilfen.com",
#     "zugradar24.com",
#     "zugrow.com",
#     "zuhausefit.com",
# ]

# print(domains[111:155])


def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
        


output=[]

for domain in domains[:50]:

    res="No" if is_registered(domain) else "Yes"
    output.append([domain,res])
    # print(domain,res)
    # time.sleep(1)


new_df=pd.DataFrame(output,columns=['Domain Ref','Availability'])

new_df.to_csv('output.csv')