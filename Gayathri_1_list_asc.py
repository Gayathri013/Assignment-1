# taking names as input and splitting the words and converting it to list
names_li = list(map(str,input().split()))
# inbuild function to sort the list in ascending order
names_li.sort()
# prints list of names in ascending order 
print(names_li)
# ["abc" , "bcd" , "cde" , "def"]