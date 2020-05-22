import pandas as pd
import ast
data=pd.read_excel('Results.xlsx')
# 34,35
xa=[20,21,22,24,25,26,27,28,31,32,34]
ya=[]
for i in range(20,36):
	# if i not in xa:
	# 	ya.append(i)
	ya.append(i)
# print(len(ya))
ol= [[0 for i in range(11)] for j in range(16)]
# xa=[20]
for i in range(1,641):
	j=0
	for a in xa :
		r=0
		for k in ya:
			# print(data.iloc[i,k],data.iloc[i,a])
			# break
			if data.iloc[i,k]==data.iloc[i,a]:
				ol[r][j]+=1 
			r+=1
		j+=1
		# break
	# break

# print(ol)

import csv
from itertools import zip_longest


d = ol

d=list(map(list, zip(*d)))
export_data = zip_longest(*d, fillvalue = '')
with open('new-matrix.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      #wr.writerow(("SIZE", "ERT","LPT ","EDD","ODD", "FDD","CGH_LST","CI","SIZE-ANN","ERT-ANN","LPT-ANN","EDD-ANN","ODD-ANN","FDD-ANN","ANN-LST",))
      wr.writerows(export_data)
myfile.close()







