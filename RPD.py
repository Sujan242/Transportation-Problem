import pandas as pd
import ast
data=pd.read_excel('Results.xlsx')
import scipy.stats as ss
ol=[]


print(data.iloc[0,34])


for i in range(1,5):

	l= data.iloc[i,2:34].values.tolist()

	op = int(data.iloc[i,34])
	print(data.iloc[i,34])

	for i in range(len(l)):
		l[i] = ((int(l[i]) - op)/op)*100

	ol.append(l)

import csv
from itertools import zip_longest


# d = ol

# d=list(map(list, zip(*d)))
# export_data = zip_longest(*d, fillvalue = '')
# with open('RPD.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
#       wr = csv.writer(myfile)
#       #wr.writerow(("SIZE", "ERT","LPT ","EDD","ODD", "FDD","CGH_LST","CI","SIZE-ANN","ERT-ANN","LPT-ANN","EDD-ANN","ODD-ANN","FDD-ANN","ANN-LST",))
#       wr.writerows(export_data)
# myfile.close()



