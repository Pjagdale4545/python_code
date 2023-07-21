# a=[1,2,3,4,5,6]
# for item in a:
#     print(item)
#     if(item==3):
#         break    #we get 1,2,3 only three numbers until condition satisfied
# print("we have finished the loop")

# a=[1,2,3,4,5,6]
# for item in a:
#     print(item)
#     if(item==3):
#        continue   
#     print("done this iteration for ", item) # third not include


#     #----------------else with for: only printed after loop is successfully executed in break statement not printed
# a=[1,2,3,4,5,6]
# for item in a:
#     print(item)
# else:
#     print("done")

#------4----------
a=[1,2,3,4,5,6]
for item in a:
    print(item)
    if(item==3):
        break    #we get 1,2,3 only three numbers until condition satisfied
else:
    print("done")  #not printed breaking loop will be not executed else
print("we have finished the loop")

#pass statment is for do nothing
for item in a:
    pass

