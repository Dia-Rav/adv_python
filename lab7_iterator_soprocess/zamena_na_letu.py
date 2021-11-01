'''
выводит тексты исправленные тексты файлов
можно было бы еще убрать лишние переносы и пробелы, но, вроде этого не было в задании
чтобы было проще различать тексты, программа выводит название (номер) файла
__next__ возвращает отредактированные тексты, сами файлы не меняются
__iter__ ничего не меняет 
'''



import os
from pathlib import Path
import re


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
        return text



    def __iter__ (self):
         return self

    def __next__ (self):
        file_path = next(self.iterable)
        print (file_path)
        text = self.norm(file_path)
        return text

a = TextLoader('sample')
os.chdir('sample') 
#выведем все файлы:
print (a.files_list)
for one in a:  
    print (one)
