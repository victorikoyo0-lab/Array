scores = [65, 82, 47, 91, 58, 73, 39, 85]

print("List:  ", scores)
print("Search:", scores.index(91))

scores.sort()
print("Sort:  ", scores)

scores.insert(4, 70)
print("Insert:", scores)

del scores[0]
print("Delete:", scores)
