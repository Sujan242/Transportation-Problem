import pandas as pd 
from collections import defaultdict
import math
import csv
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]

for insta in range(640):
	print(insta+1)
	costs=ast.literal_eval(data['Costs'].iloc[insta])
	demand=ast.literal_eval(data['Demand'].iloc[insta])
	supply=ast.literal_eval(data['Supply'].iloc[insta])
	ls=len(supply)
	ld=len(demand)
	di = 0
	instance=insta%160
	# print((instance+1)/40)
	if int((instance)/40) == 0:
		di = 1 
	elif int((instance)/40) == 1:
		di = 2
	elif int((instance)/40 )== 2:
		di = 5
	else :
		di=10
	fan = (instance%40)
	cos=0
	if int(fan/10) ==0:
		cos=20
	elif int(fan/10)==1:
		cos=100
	elif int(fan/10)==2:
		cos=500
	else:
		cos=1000

	s= f"{ld-ld%10}_{di}_{cos}_{(insta%10 +1)}"
	output.append(s)

import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [output]
export_data = zip_longest(*d, fillvalue = '')
with open('KSAM1-TOM.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Configuration"))
      wr.writerows(export_data)
myfile.close()