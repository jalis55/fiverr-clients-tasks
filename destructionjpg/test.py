import re
email = 'serebro@gmail.com'
email_split = re.search(r'(.+)@(.+)', email)
if email_split:
    email_part=list(email_split.groups())
# => ['serebro', 'gmail', 'com']
print(email_part)