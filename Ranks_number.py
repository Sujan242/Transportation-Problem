import pandas as pd
import ast
import pandas as pd 
from collections import defaultdict
import math
import csv
import copy
import json
import ast
data=pd.read_csv('Ranks.csv')
import scipy.stats as ss
ol=[]

# print(data.iloc[:,0])


for i in range(30):

	l = data.iloc[:,i].tolist()
	# print(l)
	# print(l.count("2"))
	# break
	l1=[]
	ir=0
	# print(l)
	su=0
	for j in range(1,31):
		# print(j)
		l1.append(l.count(str(j)))
		ir = ir + l.count(str(j))*j 
	ol.append(ir / sum(l1))
	# break

		# su+=l.count([str(j)])
	with open('Count_of_ranks.csv','a',newline='') as fd:
		# writer = csv.writer()
			writer = csv.writer(fd)
			writer.writerow(l1)
	# print(su)
	# print(sum(l1))
	# ol.append(l1)
with open('Count_of_ranks.csv','a',newline='') as fd:
		# writer = csv.writer()
			writer = csv.writer(fd)
			writer.writerow(ol)

o=[(sorted(ol).index(x)+1) for x in ol]
with open('Count_of_ranks.csv','a',newline='') as fd:
		# writer = csv.writer()
			writer = csv.writer(fd)
			writer.writerow(o)


# print(o)

	
# import csv
# from itertools import zip_longest
# # instance_number=range(1,641)
# d = [ol]
# d=list(map(list, zip(*d)))
# export_data = zip_longest(*d, fillvalue = '')
# with open('Count_of_ranks.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
#       wr = csv.writer(myfile)
#       # wr.writerow(("Configuration"))
#       wr.writerows(export_data)
# myfile.close()
# print(ol)