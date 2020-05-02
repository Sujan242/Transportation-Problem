import pandas as pd 
from collections import defaultdict
import math
import csv
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]

es=[]
ed=[]
for insta in range(640):
	# print(insta+1)
	costs=ast.literal_eval(data['Costs'].iloc[insta])
	demand=ast.literal_eval(data['Demand'].iloc[insta])
	supply=ast.literal_eval(data['Supply'].iloc[insta])

	ls=len(supply)
	ld=len(demand)
	if ld%10==1:
		es.append(insta)
print(es)

print(len(es))
