import zipfile
import os
archive = zipfile.ZipFile('main.zip', 'r')
archive.extractall('.')
archive.close()
ans = []
for current_dir, dirs, files in os.walk("main"): #передаем в качестве аргумента текущую директорию
    for file in files:
        if file.find('.py')>0:
            answer = current_dir.split('\\')
            ans.append (answer[-1])
            break
ans = sorted(ans)
for i in range (len(ans)):
    print (ans[i])
