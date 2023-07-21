with open("poem.txt","r") as f:
    if('twinkle' in f.read()):
        print("twinkle word is present in file")
    else:
        print("twinkle word is NOT present in file")