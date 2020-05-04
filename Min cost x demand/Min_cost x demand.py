import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast
data= pd.read_csv('input.csv')

output=[]
costs_list=[]
for instance in range(640):
	print(instance+1)
	costs=ast.literal_eval(data['Costs'].iloc[instance])
	demand=ast.literal_eval(data['Demand'].iloc[instance])
	supply=ast.literal_eval(data['Supply'].iloc[instance])
	cols = sorted(demand.keys())
	costs1=copy.deepcopy(costs)
	# print(supply['S1'])
	# break
	# costs1=copy.deepcopy(costs)

	costs2=copy.deepcopy(costs)
	costs3=copy.deepcopy(costs)
	
	            

	res = dict((k, defaultdict(int)) for k in costs)
	ls=len(supply)
	while supply : 
		sx="D"
		dy="S"
		mi=100000000
		for x in supply:
			for y in demand:
				term= costs[x][y]*min(supply[x],demand[y])
				if term < mi :
					mi=term
					sx=x
					dy=y
		# print(sx,dy)
		v=min(supply[sx],demand[dy])
		res[sx][dy]+=v
		supply[sx]-=v
		demand[dy]-=v

		if demand[dy]==0:
			del demand[dy]
		if supply[sx]==0:
			del supply[sx]

	# print(demand,supply)

	cost = 0
	for g in sorted(costs):
	    # print (g, "\t",)
	    for n in cols:
	        y = res[g][n]
	        if y != 0:
	        	pass
	            # print (y,)
	        cost += y * costs[g][n]
	        # print ("\t",)
	    # print()
	# print ("\n\nTotal Cost = ", cost)
	
	costs_list.append(cost)
	
 # 921541
import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list]
export_data = zip_longest(*d, fillvalue = '')
with open('Min cost x demand.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs"))
      wr.writerows(export_data)
myfile.close()
