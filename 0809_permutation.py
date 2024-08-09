from pprint import pprint
subset = []
for i in range(4):
    for j in range(4):
        if i != j:
            for k in range(4):
                if k != i and k != j:
                    subset.append([i,j,k])
pprint(subset)