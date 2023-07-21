oxford={
    "gift":"something giving to someone",
    "sachin" : "a good husband",
    "pooja" : "a good wife",
    "mylist":[1,2,45]

}
#print(oxford)
#print(oxford["sachin"])
#print(oxford.items()) #separate every item with parantheses

oxford.update({"sachin":"a smart and caring hubby","mylist": [2,46,78]})
for a,b in oxford.items():
    print(a,":",b)

for key in oxford.keys():#return keys
 print(key)

 #if key not in present in dictionary so use get so that not throw error give none
 print(oxford.get("notpresent"))

 #------set----
 myset={1,34,56}
 myset.add(45)
 myset.add(1)  #this not added because it is already in set
 myset.add("1") #this is string so it will be added
 print(myset)
 myset.remove(45)
 print(myset)
 print(myset.pop()) # delete random element
 print(myset)
 print(len(myset))
 myset.clear() #returns empty set
print(myset)