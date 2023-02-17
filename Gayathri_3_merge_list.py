lst1 = [19542209,4887871,1420491,626299,1805832,39865590]
lst2 = ["New York","Alabama","Hawaii","Vermont","West Virginia","California"]
merge_tuple = ()
for item1 , item2 in zip(lst1,lst2):
    merge_tuple += (item1,item2)

print(merge_tuple)
