with open ('mine.txt','r') as f:
   content=f.read()
    
content=content.replace("donkey","@#$$^&")

with open('mine.txt','w') as f:
    f.write(content)
    