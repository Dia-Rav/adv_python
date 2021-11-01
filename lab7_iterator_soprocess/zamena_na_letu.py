import zipfile
import os
from pathlib import Path
import re
import shutil




class TextLoader:
    def __init__ (self, adress):

        self.path = adress
        self.files_list = [x for x in list(os.listdir(self.path))]
        self.iterable = iter (self.files_list)

    def __len__ (self):
        return len(self.files_list)

    def __getitem__ (self, path):
        return norm(path)

    def norm (self, path):
                
        file = open(path, "r+t", encoding='utf-8')

        text = ''
        for line in file:
            line = line.lower()
            line = re.sub(r'[^\w\s]','', line) 
            text += '\n'
            text += line
        file.close()
        print (text)
        f = open(path, "w", encoding='utf-8') 
        f.write (text)
        f.close()
        f = open(path, "r", encoding='utf-8')
        return f



    def __iter__ (self):
         return self

    def __next__ (self):
        file_path = next(self.iterable)
        print (file_path)
        file = self.norm(file_path)
        return file

a = TextLoader('sample')
os.chdir('sample') 

print (a.files_list)
for one in a:  
    for line in one:
        print (line)












