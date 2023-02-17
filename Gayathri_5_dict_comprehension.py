key = [i for i in range(100,160,10)]
# created list using list comprehension
dic = {x:x/100 for x in key}
# created dictionary using dictionary comprehension 
print(dic)
