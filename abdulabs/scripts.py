import os
 
path = os.path.dirname(__file__)
for file in os.listdir(path):
    directory = os.path.join(path, file)
    if os.path.isdir(directory):
        files=os.listdir(directory)
        print(files)