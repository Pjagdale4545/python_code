#replace multiple words in the file
words=["donkey","bad","nonsense"]

with open ('mine.txt','r') as f:
   content=f.read()
   
for item in words:
   content=content.replace(item,"@#$$^&") 
   with open('mine.txt','w') as f:
    f.write(content)


